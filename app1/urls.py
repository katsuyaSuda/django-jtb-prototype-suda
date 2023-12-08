from django.urls import path

from . import views

urlpatterns = [
    # path('', views.Index.as_view(), name="index"),
    path('', views.List.as_view()),
    path('create/', views.Create.as_view(), name="create"),
    path('list/', views.List.as_view(), name="list"),
    path('export/', views.csv_export, name='csv_export'),
    path('import/', views.CsvImport.as_view(), name='csv_import'),
    path('upload/', views.upload_file_to_s3, name='upload_file_to_s3'),
    path('download/', views.download_file_from_s3_directly, name='download_file_from_s3_directly'),
]
