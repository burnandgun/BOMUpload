# -*- coding:utf-8 -*-

from django import forms
from django.utils.translation import  gettext as _
from django.core.exceptions import ValidationError


#验证上传的文件是否为excel文件


def validate_excel(value):
    if value.name.split('.')[-1] not in ['xls', 'xlsx']:
        raise ValidationError(_('Invalid File Type: %(value)s'), params={'value': value},)


class UploadExcelForm(forms.Form):
    excel = forms.FileField(validators=[validate_excel])
