
from django.urls import path
import my_db.views as mv

urlpatterns = [
path('', mv.base, name='first_page'),

path('person/create/', mv.Create_person.as_view(), name='create_person'),
path('person/get_list/', mv.List_of_persons.as_view(), name='get_list_persons'),
path('person/get/<pk>/', mv.Get_person.as_view(), name='get_person'),

path('project/create/', mv.Create_project.as_view(), name='create_project'),
path('project/get_list/', mv.List_of_projects.as_view(), name='get_list_projects' ),
path('project/get/<pk>/', mv.Get_project.as_view(), name='get_project'),
path('project/add_person/', mv.Add_person_to_project.as_view(), name='add_person'),

path('company/create/', mv.Create_company.as_view(), name='create_company'),
path('company/get/<pk>/', mv.Get_company.as_view(), name='get_company'),
path('company/get_list/', mv.List_of_companies.as_view(), name='get_list_companies'),


path('API/', mv.MarshView, name='API'),

    ]