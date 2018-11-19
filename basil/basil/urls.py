from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.TransactionCSVUploaderView.as_view(),
        name='transaction_csv_uploader'
    ),
]
