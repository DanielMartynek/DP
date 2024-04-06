from django.urls import path

from . import views




urlpatterns = [
    path("", views.home, name=""),
    path("help/",views.help,name="help"),
    path('export-csv/', views.export_csv, name='export_csv')
]
