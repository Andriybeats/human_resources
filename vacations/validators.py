from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


def validate_start_date(value):
    if value < datetime.date(2009, 1, 6):
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
