import sys

from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from employee_information.models import *

def pagination_list(request, obj_list, obj_in_page):
    page = request.GET.get('page', 1)
    paginator = Paginator(obj_list, obj_in_page)
    try:
        obj_list = paginator.page(page)
    except PageNotAnInteger:
        obj_list = paginator.page(1)
    except EmptyPage:
        obj_list = paginator.page(paginator.num_pages)

    return obj_list


def check_admin(user):
    if user.is_superuser:
        return True
    raise PermissionDenied()


def check_admin_hr(user):
    if user.is_superuser or user.is_mainHR:
        return True
    return False


def capitalize_each_word(original_str):
    result = ""
    # Split the string and get all words in a list
    list_of_words = original_str.split()
    # Iterate over all elements in list
    for elem in list_of_words:
        # capitalize first letter of each word and add to a string
        if len(result) > 0:
            result = result + " " + elem.strip().capitalize()
        else:
            result = elem.capitalize()
    # If result is still empty then return original string else returned capitalized.

    return result