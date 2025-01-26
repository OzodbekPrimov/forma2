from django.urls import path
from .views import person_forma, person_list

urlpatterns = [
    path('', person_forma, name='person-form'),
    path('list/', person_list, name='person-list'),
]