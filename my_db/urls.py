
from django.urls import path
import my_db.views as mv

urlpatterns = [
path('', mv.base),
path('add_candidate/', mv.add_candidate),

path('create_person/', mv.Create_person.as_view(), name='create_person'),
path('create_project/', mv.create_project, ),
path('create_company/', mv.create_company),
path('edit_person/', mv.edit_person),
path('get_list_of_persons/', mv.get_list_of_persons),
path('get_list_of_person_with_filter/', mv.get_list_of_person_with_filter),
path('get_persons_of_project/', mv.get_persons_of_project),
path('get_sum_of_persons_in_project/', mv.get_sum_of_persons_in_project),
path('count_person_in_project/', mv.count_person_in_project),




    ]