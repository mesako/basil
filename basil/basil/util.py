from contextlib import contextmanager
import csv
import io
import typing

from wrapt import ObjectProxy


class SeekableReader(ObjectProxy):
    __slots__ = ()

    def __init__(self, raw):
        if not (hasattr(raw, 'peek') or raw.seekable()):
            raise TypeError
        super().__init__(raw)

    def peek(self, size=0):
        if hasattr(self.__wrapped__, 'peek'):
            return self.__wrapped__.peek(size)
        with self.roll_back_stream_position():
            return self.read(size)

@contextmanager
def roll_back_stream_position(raw_io: io.IOBase) -> typing.Generator[io.IOBase, None, None]:
    """Context manager to return a seekable IO object back to the stream position it had upon entering the context."""
    current_stream_position = raw_io.tell()
    try:
        yield raw_io
    finally:
        raw_io.seek(current_stream_position)


class PeekableReader(ObjectProxy):
    __slots__ = ()

    def __init__(self, raw):
        if not (hasattr(raw, 'peek') or raw.seekable()):
            raise TypeError
        super().__init__(raw)

    def peek(self, size=0):
        if hasattr(self.__wrapped__, 'peek'):
            return self.__wrapped__.peek(size)
        with self.roll_back_stream_position():
            return self.read(size)

    @contextmanager
    def roll_back_stream_position(self):
        current_stream_position = self.tell()
        try:
            yield
        finally:
            self.seek(current_stream_position)


def FieldNameFindingCSVDictReader(csvfile, *, fieldnames=None, dialect=None, **dict_reader_kwargs):
    sniffer = csv.Sniffer()

    csvfile = PeekableReader(csvfile)
    dialect = dialect or sniffer.sniff(csvfile.peek(1024)) or 'excel'
    dict_reader_kwargs['dialect'] = dialect

    #fieldnames = set(kwargs.pop('fieldnames') or ())# Headers might not be present at all
    fieldnames_set = set(fieldnames or ())
    csv_reader = csv.reader(csvfile, dialect=dialect)
    while True:
        with csvfile.roll_back_stream_position():
            dict_reader = csv.DictReader(csvfile, **dict_reader_kwargs)
            row = next(dict_reader, None)
            latest_stream_position = csvfile.tell()
        if row is None:
            csvfile.seek(0)
            return csv.DictReader(csvfile, fieldnames=fieldnames, **dict_reader_kwargs)
        if fieldnames_set.issubset(dict_reader.fieldnames) and (fieldnames_set or sniffer.has_header(csvfile.peek(10 * (latest_stream_position - csvfile.tell())))):
            return csv.DictReader(csvfile, **dict_reader_kwargs)
        next(csv_reader)
