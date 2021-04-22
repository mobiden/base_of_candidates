from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from my_db.models import Person, Project, Company
from django.db.models import Max, Count, Avg
from .forms import create_personForm


def base(request):
    return render(request, 'my_db_views/db_base_main.html')

class Create_person(View):
    def get(self, request):
        form = create_personForm()
        return render(request, 'my_db_views/Person/create_person.html', {'form': form})

    @csrf_exempt
    def post(self, request):
        form = create_personForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            person = Person()
            person.last_name = form.cleaned_data["last_name"]
            person.first_name = form.cleaned_data["first_name"]
            person.middle_name = form.cleaned_data["middle_name"]
            person.mob_phone = form.cleaned_data["mob_phone"]
            person.sec_phone = form.cleaned_data["sec_phone"]
            person.e_mail = form.cleaned_data["e_mail"]
            person.city = form.cleaned_data["city"]
            person.messenger = form.cleaned_data["messenger"]
            person.messenger_id = form.cleaned_data["messenger_id"]
            person.current_company = form.cleaned_data["current_company"]
            person.position = form.cleaned_data["position"]
            person.comments = form.cleaned_data["comments"]
            try:
                person.save()
            except:
                return render(request, 'my_db_views/Person/create_person.html', {'form': form})
            else:
                print('Done')
            return render(request, 'my_db_views/db_base_main.html')
        else:
            return render(request, 'my_db_views/Person/create_person.html', {'form': form})



def create_company(request):
    company = Company()
    company.company_name = input('Название компании: ')
    company.city = input('Город: ')
    company.phone = input('Телефон: ')
    if company.phone == '':
        company.phone = None
    company.save()
    que = input('Еще? ')
    if que.lower() == 'y':
        create_company(request)
    return HttpResponse('Ok')

def create_project(request):
    project = Project()
    project.project_name = input('Название проекта: ')
    project.vacancy = input('Название вакансии: ')
    client = input('Заказчик: ')
    client = Company.objects.get(pk = client)
    project.client = client
    project.save()
    return HttpResponse('Ok')

def add_candidate(request):
    project = Project.objects.get(pk = 2)
    cand = input("Фамилия, Имя? ").split()
    candidate = Person.objects.get(last_name=cand[0], first_name=cand[1])
    project.persons.add(candidate)
    project.save()
    return HttpResponse('Ok')

def edit_person(request):
    cand = input('Фамилия, Имя: ').split()
    cand = Person.objects.get(last_name=cand[0], first_name=cand[1])
    l_name = input("Введите новую фамилию: ")
    if l_name != '':
        cand.last_name = l_name
    f_name = input("Введите новое имя: ")
    if f_name != '':
        cand.first_name = f_name
    cand.save()
    return HttpResponse('Ok')

def get_list_of_persons(request):
    lists = Person.objects.all()
    return HttpResponse(lists.values('last_name', 'first_name', 'mob_phone'))

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