from django import forms
from .models import Users


class UserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['name', 'email', 'telephone', 'group']
        widgets = {
            'group': forms.RadioSelect()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not field_name=='group':
                field.widget.attrs.setdefault('class','form-control')
        self.fields['telephone'].widget.attrs.update({'data-mask': '(00) 00000-0000'})
