from . import views

from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"), name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name='base_pages/login.html', redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),

    # DEPARTMENT URL
    path('departments', views.departments, name="department-page"),
    path('manage_departments', views.manage_departments, name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    # POSITION URL
    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
    # STATUS URL
    path('statuses', views.statuses, name="status-page"),
    path('manage_statuses', views.manage_statuses, name="manage_statuses-page"),
    path('save_status', views.save_status, name="save-status-page"),
    path('delete_status', views.delete_status, name="delete-status"),
    # EMPLOYEE URL
    path('employees', views.employees, name="employee-page"),
    path('manage_employees', views.manage_employees, name="manage_employees-page"),
    path('editor_employees', views.editor_employee, name="editor_employees-page"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('edit_employee', views.edit_employee, name="edit-employee-page"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('search', views.search_employee, name="employee-search-page"),

    path('employee/<int:pk>', views.details_employee, name="employee-details-page"),
    path('employees/<int:pk>', views.employees_by_department, name="employee-department-page"),


]
