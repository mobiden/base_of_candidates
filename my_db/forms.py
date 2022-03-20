from django import forms
from my_db.models import Project, Company



class create_companyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['creating_date']


class create_ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['creating_date', 'pr_people']
