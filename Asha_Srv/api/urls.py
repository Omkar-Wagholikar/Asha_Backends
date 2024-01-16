from django.urls import path
from . import views

urlpatterns = [
    path("get/", views.getData),
    path("add/", views.addQuery),
    path("answer/", views.answer),
    path('reportError/', views.reportError),
    path('api/pdf/<str:filename>/', views.PdfFileView.as_view(), name='pdf_file_view'),
]