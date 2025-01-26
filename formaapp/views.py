from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person
# Create your views here.

def person_forma(request):
    form = PersonForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect("person-list")
    ctx = {
        'form':form
    }
    return render(request, 'form.html',ctx)

def person_list(request):
    people = Person.objects.all()
    ctx = {
        'people':people
    }
    return render(request, 'table.html',ctx)
