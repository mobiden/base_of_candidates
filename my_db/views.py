from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from my_db.models import Person, Project, Company, Projects_people
from django.db.models import Max, Count, Avg
from .forms import create_personForm, create_companyForm, create_ProjectForm
from .schemas import REVIEW_SCHEMA, ReviewSchema
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from marshmallow import ValidationError as MarError
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView


@login_required
def base(request):
    return render(request, 'my_db_views/db_base_main.html')

class Create_person(LoginRequiredMixin, View):

    def get(self, request):
        form = create_personForm()
        return render(request, 'Person/create_person.html', {'form': form})

    def post(self, request):
        form = create_personForm(request.POST)
        if form.is_valid():
            form.instance.creating_date = datetime.now()
            form.clean()
            try:
                form.save()
            except:
                return render(request, 'Person/create_person.html', {'form': form})
            else:
                success = 'Кандидат внесен в базу'
        else:
            success = 'Некорректные данные'
            render(request, 'Person/create_person.html', {
                'form': form, 'success': success })
        return render(request, 'Person/edit_person.html', {
                'form': form, 'success': success, })


class List_of_persons(LoginRequiredMixin, ListView):
    model = Person
    def get_queryset(self):

        if True:
#        if self.request.user.is_superuser:
            return Person.objects.get_queryset()
    template_name = 'Person/Person_list.html'

class Get_person(LoginRequiredMixin, View):

    def get(self, request, pk):
        person = Person.objects.get(pk = pk)
        form = create_personForm(instance=person)
        to_add = True
        return render(request, 'Person/edit_person.html', {'form': form, 'id': int(pk)})

    def post(self, request):
        form = create_personForm(request.POST)
        if form.is_valid():
            form.instance.creating_date = datetime.now()
            form.clean()
            try:
                form.save()
            except:
                return render(request, 'Person/create_person.html', {'form': form})
            else:
                success = 'Кандидат внесен в базу'
            return render(request, 'Person/edit_person.html', {'form': form, 'success': success})
        else:
            success = 'Некорректные данные'
            return render(request, 'Person/create_person.html', {'form': form, 'success': success})


class Create_company(LoginRequiredMixin, CreateView):
    model = Company
    fields = [
        'company_name',
        'city',
        'phone',
        'comments',
        'id'

    ]
    template_name = 'Company/company_form.html'

    def form_valid(self, form):
        form.instance.creating_date = datetime.now()
        return super().form_valid(form)

    success_url = '/db/'



class List_of_companies(LoginRequiredMixin, ListView):
    model = Company
    def get_queryset(self):
        if True:
#        if self.request.user.is_superuser:

            return Company.objects.values('company_name', 'city', 'phone', 'comments', 'id')

    template_name = 'Company/company_list.html'


class Get_company(LoginRequiredMixin, View):

    def get(self, request, pk):
        company = Company.objects.get(pk= pk)
        form = create_companyForm(instance=company)
        return render(request, 'Company/create_company.html', {'form': form})

    def post(self, request):
        form = create_companyForm(request.POST)
        if form.is_valid():
            form.clean()
            try:
                form.save()
            except:
                return render(request, 'Company/create_company.html', {'form': form})
            else:
                success = 'Change of company successfully saved '
        else:
            success = 'Incorrect data'
        return render(request, 'Company/create_company.html', {'form': form, 'success': success})


class Create_project(LoginRequiredMixin, View):
    def get(self, request):
        form = create_ProjectForm()
        return render(request, 'Project/create_project.html', {'form': form})


    def post(self, request):
        form = create_ProjectForm(request.POST)
        if form.is_valid():
            form.clean()
            try:
                form.save()
            except:
                success = 'Данные не сохранены'
                return render(request, 'Project/create_project.html', {'form': form, 'success': success})

            success = 'Проект внесен'
            return render(request, 'Project/edit_project.html', {'form': form, 'success': success})
        else:
            success = "Некорректные данные"
            return render(request, 'Project/create_project.html', {'form': form, 'success': success})


class List_of_projects(LoginRequiredMixin, ListView):
    model = Project

    def get_queryset(self):
        if True:
#        if self.request.user.is_superuser:
            return Project.objects.get_queryset()

    template_name = 'Project/project_list.html'


class Get_project(LoginRequiredMixin, View):
    def get(self, request, pk):
        project = Project.objects.get(pk= pk)
        form = create_ProjectForm(instance=project)

        project_people = Person.objects.filter(long_list_persons__project_id=pk)
        project_people2 = project.pr_people.all()
        return render(request, 'Project/edit_project.html',
                      {'form': form, 'pr_p': project_people2})

    def post(self, request):
        form = create_ProjectForm(request.POST)
        if form.is_valid():
            form.clean()
            try:
                form.save()
            except:
                return render(request, 'Project/create_project.html', {'form': form})
            else:
                success = 'Change of project successfully saved '
        else:
            success = 'Incorrect data'
        return render(request, 'Project/create_project.html', {'form': form, 'success': success})


class Add_person_to_project(LoginRequiredMixin, ListView):

    def get(self, request, pk):
        #       from pdb import set_trace; set_trace()
        projects = Project.objects.all()
        return render(request, 'Project/project_list_for_added.html', context={
        'projects':projects, 'person_pk':pk,
         })


    def post(self, request, pk):
        pr_id = request.POST.get("pr_id")
        project_people = Projects_people()
        project_people.project = Project.objects.get(pk = pr_id)
        project_people.people = Person.objects.get(pk = pk)



        try:
            project_people.save()
            print ('added')
        except:
            success = 'Данные не сохранены'
            return redirect('first_page')

        success = 'Candidate successfuly added'
        return redirect('first_page')
 #       return HttpResponse('Candidate successfuly added')





def get_sum_of_persons_in_project(request):
    lists = Project.objects.get(pk=2).persons.count()
    return HttpResponse(lists)

def max_avg_phone(request):
# aggregate
    q = Person.objects.aggregate(
        dif=Max('mob_phone', output_field=models.FloatField())
                                - Avg('mob_phone',output_field=models.FloatField())
                                )
    return HttpResponse(q['dif'])

def count_person_in_project(request):
# annotation
    q = Project.objects.annotate(Count('persons')).filter(project_name__contains='омме')
    return render(request, 'my_db_views/index.html')

class SchemaView(View):
    def post(self, request):
        try:
            document = json.loads(request.body)
            validate(document, REVIEW_SCHEMA)
            return JsonResponse (document, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': "Invalid JSON"}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)



class MarshView(View):
    def post(self, request):
        try:
            document = json.load(request.body)
            schema = ReviewSchema(strict=True)
            data = schema(document)
            return JsonResponse (data.data, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': "Invalid JSON"}, status=400)
        except MarError as exc:
            return JsonResponse({'errors': exc.message}, status=400)
