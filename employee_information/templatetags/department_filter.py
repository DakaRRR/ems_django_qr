from django import template

from employee_information.models import Department

register = template.Library()


@register.simple_tag
def get_departments():
    department = Department.objects.all()
    return department