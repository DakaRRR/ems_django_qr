import json
import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from .methods import *


def error_404(request, exception):
    # page not found
    return render(request, 'errors/404.html')


def error_500(request, *args, **argv):
    # page error
    return render(request, 'errors/500.html', status=500)


def error_403(request, exception):
    # permission_denied
    return render(request, 'errors/403.html')


def error_400(request, exception):
    # bad request
    return render(request, 'errors/400.html')


@login_required
def search_employee(request):
    if request.POST:
        employees_searched_list = {}
        fullname = request.POST['fullname']
        if fullname != '':
            capitalize_name = capitalize_each_word(fullname)
            employees_searched_list = Employees.objects.filter(
                Q(fullname__icontains=fullname) | Q(firstname__icontains=fullname) | Q(
                    lastname__icontains=fullname) | Q(middlename__icontains=fullname) | Q(
                    fullname__icontains=capitalize_name) | Q(firstname__icontains=capitalize_name) | Q(
                    lastname__icontains=capitalize_name) | Q(middlename__icontains=capitalize_name)).order_by(
                'department_id__sort_id', 'position_id__sort_id', 'fullname')

        context = {
            'page_title': 'Поиск сотрудников ' + fullname,
            'employees': employees_searched_list,
        }
        return render(request, 'employee_information/employees.html', context)


# Login
def login_user(request):
    logout(request)
    resp = {"status": 'failed', 'msg': ''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status'] = 'success'
            else:
                resp['msg'] = "Не верный логин или пароль"
        else:
            resp['msg'] = "Не верный логин или пароль"
    return HttpResponse(json.dumps(resp), content_type='application/json')


# Logout
def logoutuser(request):
    logout(request)
    return redirect('/')


# Create your views here.
@login_required
def home(request):
    context = {
        'page_title': 'Главная',
        'employees': employees,
        'total_department': len(Department.objects.all()),
        'total_position': len(Position.objects.all()),
        'total_employee': len(Employees.objects.all()),
    }
    return render(request, 'base_pages/home.html', context)


# Departments
@login_required
def departments(request):
    department_list = Department.objects.all()
    context = {
        'page_title': 'Филиалы',
        'departments': department_list,
    }
    return render(request, 'employee_information/departments.html', context)


@login_required
def manage_departments(request):
    department = {}
    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()

    context = {
        'department': department
    }
    return render(request, 'employee_information/manage_department.html', context)


@login_required
def save_department(request):
    data = request.POST
    resp = {'status': 'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0:
            department = Department.objects.get(id=data['id'])
        else:
            department = Department()
        department.name = data['name']
        if data['sort_id'].isnumeric():
            department.sort_id = data['sort_id']
        else:
            department.sort_id = 99
        department.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_department(request):
    data = request.POST
    resp = {'status': ''}
    try:
        Department.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


# Positions
@login_required
def positions(request):
    position_list = Position.objects.all().order_by('sort_id', 'name')
    position_list = pagination_list(request, position_list, 20)
    context = {
        'page_title': 'Должности',
        'positions': position_list,
    }
    return render(request, 'employee_information/positions.html', context)


@login_required
def manage_positions(request):
    position = {}
    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()

    context = {
        'position': position
    }
    return render(request, 'employee_information/manage_position.html', context)


@login_required
def save_position(request):
    data = request.POST
    resp = {'status': 'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0:
            position = Position.objects.get(id=data['id'])
        else:
            position = Position()
        position.name = data['name']
        position.sort_id = data['sort_id']
        if data['sort_id'].isnumeric():
            position.sort_id = data['sort_id']
        else:
            position.sort_id = 999
        position.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_position(request):
    data = request.POST
    resp = {'status': ''}
    try:
        Position.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
# Statuses
def statuses(request):
    status_list = StatusEmployee.objects.all()
    context = {
        'page_title': 'Статусы',
        'statuses': status_list,
    }
    return render(request, 'employee_information/statuses.html', context)


@login_required
def manage_statuses(request):
    emp_status = {}
    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            emp_status = StatusEmployee.objects.filter(id=id).first()

    context = {
        'status': emp_status
    }
    return render(request, 'employee_information/manage_status.html', context)


@login_required
def save_status(request):
    data = request.POST
    resp = {'status': 'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0:
            save_status = StatusEmployee.objects.filter(id=data['id']).update(name=data['name'])
        else:
            save_status = StatusEmployee(name=data['name'])

            save_status.save()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'

    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_status(request):
    data = request.POST
    resp = {'status': ''}
    try:
        StatusEmployee.objects.filter(id=data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
# Employees
def employees(request):
    if check_admin_hr(request.user):
        employee_list = Employees.objects.all().order_by('department_id__sort_id', 'position_id__sort_id', 'lastname', 'firstname', 'middlename')
        employee_list_count = len(employee_list)
        page_title = 'Список сотрудников всех подразделений' + ' (' + str(employee_list_count) + ')'
    else:
        user_dep = request.user.department_id
        department = Department.objects.get(name=user_dep)
        employee_list = Employees.objects.filter(department_id=user_dep).order_by('position_id__sort_id', 'lastname', 'firstname', 'middlename')
        employee_list_count = len(employee_list)
        page_title = 'Список сотрудников ' + department.name + ' (' + str(employee_list_count) + ')'

    employee_list = pagination_list(request, employee_list, 20)
    context = {
        'page_title': page_title,
        'employees': employee_list,
    }
    return render(request, 'employee_information/employees.html', context)


@login_required
def employees_by_department(request, pk):
    department = Department.objects.get(id=pk)
    employee_list = Employees.objects.filter(department_id__id=pk).order_by('position_id__sort_id', 'lastname', 'firstname', 'middlename')
    employee_list = pagination_list(request, employee_list, 20)
    employee_list_count = len(Employees.objects.filter(department_id__id=pk))
    context = {
        'page_title': 'Список сотрудников ' + department.name + ' ' + str(employee_list_count),
        'employees': employee_list,
    }
    return render(request, 'employee_information/employees.html', context)


@login_required
def manage_employees(request):
    employee = {}
    departments = Department.objects.all()
    positions = Position.objects.all()
    statuses = StatusEmployee.objects.all()
    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee': employee,
        'departments': departments,
        'positions': positions,
        'statuses': statuses
    }
    return render(request, 'employee_information/manage_employee.html', context)


@login_required
def editor_employee(request):
    employee = {}
    departments = Department.objects.all()
    positions = Position.objects.all()
    statuses = StatusEmployee.objects.all()
    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee': employee,
        'departments': departments,
        'positions': positions,
        'statuses': statuses
    }
    return render(request, 'employee_information/edit_employee.html', context)


@login_required
def edit_employee(request):
    data = request.POST
    resp = {'status': 'failed'}
    user_dep = request.user.department_id

    try:
        employee = Employees.objects.get(id=data['id'])
        pos = Position.objects.filter(id=data['position_id']).first()
        stat = StatusEmployee.objects.filter(id=data['status_id']).first()

        if len(request.FILES) != 0:
            if employee.profile_image:
                os.remove(employee.profile_image.path)
            employee.profile_image = request.FILES['profile_image']

        employee.firstname = data['firstname']
        employee.middlename = data['middlename']
        employee.lastname = data['lastname']

        employee.fullname = data['lastname'] + ' ' + data['firstname'] + ' ' + data['middlename']

        if check_admin_hr(request.user):
            employee.department_id = Department.objects.filter(id=data['department_id']).first()
        else:
            employee.department_id = user_dep
        employee.position_id = pos
        employee.status_id = stat

        employee.save()

        resp['status'] = 'success'
    except Exception:
        resp['status'] = 'failed'
        print(Exception)
        print(json.dumps({"firstname": data['firstname'], "middlename": data['middlename'],
                          "lastname": data['lastname'],
                          "profile_image": data('profile_image'),
                          "department_id": data['department_id'],
                          "position_id": data['position_id'], "status_id": data['status_id']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def save_employee(request):
    data = request.POST
    resp = {'status': 'failed'}
    user_dep = request.user.department_id

    try:
        employee = Employees()

        pos = Position.objects.filter(id=data['position_id']).first()
        stat = StatusEmployee.objects.filter(id=data['status_id']).first()

        if len(request.FILES) != 0:
            employee.profile_image = request.FILES['profile_image']

        employee.firstname = data['firstname']
        employee.middlename = data['middlename']
        employee.lastname = data['lastname']

        employee.fullname = data['lastname'] + ' ' + data['firstname'] + ' ' + data['middlename']

        if check_admin_hr(request.user):
            employee.department_id = Department.objects.filter(id=data['department_id']).first()
        else:
            employee.department_id = user_dep
        employee.position_id = pos
        employee.status_id = stat
        employee.save()
        employee.generate_qr()

        resp['status'] = 'success'
    except Exception:
        resp['status'] = 'failed'
        print(Exception)
        print(json.dumps({"firstname": data['firstname'], "middlename": data['middlename'],
                          "lastname": data['lastname'], "fullname": data['fullname'],
                          "profile_image": data('profile_image'),
                          "department_id": data['department_id'],
                          "position_id": data['position_id'], "status_id": data['status_id']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_employee(request):
    data = request.POST
    employee = Employees.objects.get(id=data['id'])
    resp = {'status': ''}
    try:
        if employee.profile_image:
            os.remove(employee.profile_image.path)
        os.remove(employee.qr_code.path)
        employee.delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


def details_employee(request, pk):
    employee = Employees.objects.get(id=pk)
    departments = Department.objects.all()
    positions = Position.objects.all()
    statuses = StatusEmployee.objects.all()

    context = {
        'employee': employee,
        'departments': departments,
        'positions': positions,
        'statuses': statuses
    }
    return render(request, 'employee_information/employee_details.html', context)


