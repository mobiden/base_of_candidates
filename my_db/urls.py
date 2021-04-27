
from django.urls import path
import my_db.views as mv

urlpatterns = [
path('', mv.base, name='first_page'),

path('person/create/', mv.Create_person.as_view(), name='create_person'),
path('person/get_list/', mv.List_of_persons.as_view(), name='get_list_persons'),
path('person/<pk>/', mv.Get_person.as_view(), name='get_person'),
path('project/create/', mv.Create_project.as_view(), name='create_project' ),
path('company/create/', mv.Create_company.as_view(), name='create_company'),

path('add_candidate/', mv.add_candidate),
path('edit_person/', mv.edit_person),
path('get_list_of_person_with_filter/', mv.get_list_of_person_with_filter),
path('get_persons_of_project/', mv.get_persons_of_project),
path('get_sum_of_persons_in_project/', mv.get_sum_of_persons_in_project),
path('count_person_in_project/', mv.count_person_in_project),
path('API/', mv.MarshView, name='API'),

    ]