from django import template


register = template.Library()


@register.simple_tag
def get_user_role(request):
    if request.user.is_superuser or request.user.is_mainHR:
        return True
    return False
