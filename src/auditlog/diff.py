from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model


def model_instance_diff(old, new):
    """
    Calculate the differences between two model instances. One of the instances may be None (i.e., a newly
    created model or deleted model). This will cause all fields with a value to have changed (from None).
    """

    if not(old is None or isinstance(old, Model)):
        raise TypeError('The supplied old instance is not a valid model instance.')
    if not(new is None or isinstance(new, Model)):
        raise TypeError('The supplied new instance is not a valid model instance.')

    diff = {}

    if old is not None and new is not None:
        fields = set(old._meta.fields + new._meta.fields)
    elif old is not None:
        fields = set(old._meta.fields)
    elif new is not None:
        fields = set(new._meta.fields)
    else:
        fields = set()

    for field in fields:
        try:
            old_value = getattr(old, field.name, None)
        except ObjectDoesNotExist:
            old_value = None
        else:
            old_value = unicode(old_value) if type(old_value) is not dict else old_value

        try:
            new_value = getattr(new, field.name, None)
        except ObjectDoesNotExist:
            new_value = None
        else:
            new_value = unicode(new_value) if type(new_value) is not dict else new_value

        # Generic IPAddress field stores empty string as None
        if old_value == 'None' and new_value == '':
            continue

        # JSONield stores sets default to '[]' which can be ignored
        if old_value == 'None' and new_value == '[]':
            continue

        if cmp(old_value, new_value) != 0:
            diff[field.name] = (old_value, new_value)

    if len(diff) == 0:
        diff = None

    return diff
