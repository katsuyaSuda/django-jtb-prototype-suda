from django.urls import path

from . import views

urlpatterns = [
    # path('', views.Index.as_view(), name="index"),
    path('', views.List.as_view()),
    path('create/', views.Create.as_view(), name="create"),
]
