import django.forms


class TransactionCSVUploaderForm(django.forms.Form):
    transaction_csv_file = django.forms.FileField(help_text='A CSV file containing rows of transactions.')
