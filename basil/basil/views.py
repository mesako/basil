from tempfile import NamedTemporaryFile

from django.views.generic import FormView

from . import transaction_adaptor
from .forms import TransactionCSVUploaderForm


class TransactionCSVUploaderView(FormView):
    form_class = TransactionCSVUploaderForm
    template_name = 'basil/transaction_csv_uploader_form.html'
    # template_engine = None
    # response_class = TemplateResponse
    # content_type = None

    def form_valid(self, form):
        with NamedTemporaryFile(mode='wb+', delete=True) as temporary_file:
            for chunk in form.cleaned_data['transaction_csv_file'].chunks():
                temporary_file.write(chunk)
            temporary_file.seek(0)
            transaction_list = transaction_adaptor.discover_adaptor(temporary_file.name)
        return self.response_class(
            request=self.request,
            template=['basil/transaction_upload_response.html'],
            context={'transaction_list': transaction_list},
            using=self.template_engine,
        )
