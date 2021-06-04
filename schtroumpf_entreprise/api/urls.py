from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_employee',views.form_employe, name='form_e'),
    path('listEmployees', views.listEmployes, name='list_e'),
    path('searchEmploye', views.searchEmploye, name='search_e'),
    path('updateEmploye/<int:id>', views.updateEmploye, name='update_e'),
    path('deleteEmploye/<int:id>', views.deleteEmploye, name='delete_e'),
]
