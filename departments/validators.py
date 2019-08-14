from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_only_letters(value):
    if not value.isalpha() == True :
        raise ValidationError(
            _('%(value)s musn\'t include numbers'),
            params={'value': value},
        )
