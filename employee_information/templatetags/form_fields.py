from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag
def b4_form_field(form, field_name, **kwargs):
    field_obj = form[field_name]
    field_attrs = form.fields[field_name]
    type = kwargs.get('type', 'text').lower()  # default input type is <input type="text">
    autocomplete = kwargs.get('autocomplete', 'on').lower()  # default input autocomplete is "on"
    label_for = field_obj.id_for_label
    label_text = field_obj.label
    id_ = field_obj.id_for_label
    name = field_obj.name
    value = field_obj.value if isinstance(field_obj.value, str) else ''

    autocomplete = "on" if autocomplete == 'on' else 'off'
    required = "required" if field_attrs.required else ''
    disabled = "disabled" if field_attrs.disabled else ''
    help_text = f"<small class='form-text text-muted'>{field_obj.help_text}</small>" if field_obj.help_text else ''
    if type == 'checkbox':
        html = f"""
                <div class="form-group mb-3">
                    <label for="{label_for}" class="control-label">{label_text}</label>
                    <input type="checkbox" name="{name}"  id="{id_}"  value="{value}" {disabled} {required}>
                    {help_text}
                </div>
        """
    else:
        html = f"""
                <div class="form-group mb-3">
                   <label for="{label_for}" class="control-label">{label_text}</label>
                   <input class="form-control form-control-sm rounded-0" autocomplete="{autocomplete}" type="{type}" id="{id_}" name="{name}" value="{value}" {disabled} {required}>
                   {help_text}
                </div>
        """
    return mark_safe(html)


@register.simple_tag
def b4_form_field_instance(form, field_name, inst_value, type, **kwargs):
    field_obj = form[field_name]
    field_attrs = form.fields[field_name]
    type = kwargs.get('type', 'text').lower()  # default input type is <input type="text">
    autocomplete = kwargs.get('autocomplete', 'on').lower()  # default input autocomplete is "on"
    label_for = field_obj.id_for_label
    label_text = field_obj.label
    id_ = field_obj.id_for_label
    name = field_obj.name
    value = inst_value
    autocomplete = "on" if autocomplete == 'on' else 'off'
    required = "required" if field_attrs.required else ''
    disabled = "disabled" if field_attrs.disabled else ''
    help_text = f"<small class='form-text text-muted'>{field_obj.help_text}</small>" if field_obj.help_text else ''
    if type == 'checkbox':
        html = f"""
                <div class="form-group mb-3">
                    <label for="{label_for}" class="control-label">{label_text}</label>
                    <input type="checkbox" name="{name}"  id="{id_}"  value="{value}" {disabled} {required}>
                    {help_text}
                </div>
        """
    else:
        html = f"""
                <div class="form-group mb-3">
                   <label for="{label_for}" class="control-label">{label_text}</label>
                   <input class="form-control form-control-sm rounded-0" autocomplete="{autocomplete}" type="{type}" id="{id_}" name="{name}" value="{value}" {disabled} {required}>
                   {help_text}
                </div>
        """
    return mark_safe(html)
