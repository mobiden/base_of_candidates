from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from my_db.models import Person, Project, Company
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
        return render(request, 'my_db_views/Person/create_person.html', {'form': form})

    def post(self, request):
        form = create_personForm(request.POST)
        if form.is_valid():
            form.instance.creating_date = datetime.now()
            form.clean()
            try:
                form.save()
            except:
                return render(request, 'my_db_views/Person/create_person.html', {'form': form})
            else:
                success = 'Кандидат внесен в базу'
            return render(request, 'my_db_views/Person/create_person.html', {'form': form, 'success': success})
        else:
            success = 'Некорректные данные'
            return render(request, 'my_db_views/Person/create_person.html', {'form': form, 'success': success})


class List_of_persons(LoginRequiredMixin, ListView):
    model = Person
    def get_queryset(self):
        if True:
#        if self.request.user.is_superuser:
            return Person.objects.values('last_name', 'first_name', 'current_company', 'id')

    template_name = 'Person/Person_list.html'

class Get_person(LoginRequiredMixin, View):

    def get(self, request, pk):
        person = Person.objects.get(pk = pk)
        form = create_personForm(instance=person)
        return render(request, 'my_db_views/Person/create_person.html', {'form': form})

    def post(self, request):
        form = create_personForm(request.POST)
        if form.is_valid():
            form.clean()
            try:
                form.save()
            except:
                return render(request, 'my_db_views/Person/create_person.html', {'form': form})
            else:
                success = 'Кандидат внесен в базу'
            return render(request, 'my_db_views/Person/create_person.html', {'form': form, 'success': success})
        else:
            success = 'Некорректные данные'
            return render(request, 'my_db_views/Person/create_person.html', {'form': form, 'success': success})


class Create_company(LoginRequiredMixin, CreateView):
    model = Company
    fields = [
        'company_name',
        'city',
        'phone',
    ]
    template_name = 'Company/company_form.html'

    def form_valid(self, form):
        form.instance.creating_date = datetime.now()
        return super().form_valid(form)

    success_url = '/db/'

"""
    def get(self, request):
        form = create_companyForm()
        return render(request, 'my_db_views/Company/create_company.html', {'form': form})


    def post(self, request):
        form = create_companyForm(request.POST)
        if form.is_valid():
            form.clean()
            try:
                form.save()
            except:
                success = 'Данные не сохранены'
                return render(request, 'my_db_views/Company/create_company.html', {'form': form, 'success': success})

            success = 'Компания внесена'
            return render(request, 'my_db_views/Company/create_company.html', {'form': form, 'success': success})
        else:
            success = "Некорректные данные"
            return render(request, 'my_db_views/Company/create_company.html', {'form': form, 'success': success})
"""

class List_of_companies(LoginRequiredMixin, ListView):
    model = Company
    def get_queryset(self):
        if True:
#        if self.request.user.is_superuser:
            return Company.objects.values('company_name', 'city', 'phone', 'id')

    template_name = 'Person/Person_list.html'

class Create_project(LoginRequiredMixin, View):
    def get(self, request):
        form = create_ProjectForm()
        return render(request, 'my_db_views/Project/create_project.html', {'form': form})


    def post(self, request):
        form = create_ProjectForm(request.POST)
        if form.is_valid():
            form.clean()
            try:
                form.save()
            except:
                success = 'Данные не сохранены'
                return render(request, 'my_db_views/Project/create_project.html', {'form': form, 'success': success})

            success = 'Компания внесена'
            return render(request, 'my_db_views/Project/create_project.html', {'form': form, 'success': success})
        else:
            success = "Некорректные данные"
            return render(request, 'my_db_views/Project/create_project.html', {'form': form, 'success': success})





def add_candidate(request):
    project = Project.objects.get(pk = 2)
    cand = input("Фамилия, Имя? ").split()
    candidate = Person.objects.get(last_name=cand[0], first_name=cand[1])
    project.persons.add(candidate)
    project.save()
    return HttpResponse('Ok')






def get_list_of_person_with_filter(request):
    query = input('что ищем? ')
    lists = Project.objects.filter(persons__last_name__contains=query)
    return HttpResponse(lists.values('vacancy', 'comments')[:1])

def get_persons_of_project(request):
    lists = Project.objects.get(pk = 1)
    return HttpResponse(lists.persons.all().values('last_name', 'first_name'))

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

def topic_details(request, pk):
    return render(request, 'my_db_views/topic_details.html')


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
