from django import forms
from my_db.models import Person, Project, Company


class create_personForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['last_name',
                  'first_name',
                  'middle_name',
                  'mob_phone',
                  'sec_phone',
                  'e_mail',
                  'city',
                  'messenger',
                  'messenger_id',
                  'current_company',
                  'position',
                  'comments',
                  'resume',
                  ]

class create_companyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'city',
            'phone',
        ]

class create_ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'client',
            'project_name',
            'vacancy',
            'comments',
        ]