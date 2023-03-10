from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from classes.models import Classrooms, Persons

# Create your views here.

def homePage(request, name, user_id):
    person = Persons.objects.filter(user_id=user_id)
    lst = set()
    for i in person:
        class_no = i.classroom_id.classroom_id
        print(class_no)
        class_names = Classrooms.objects.get(classroom_id = class_no)
        lst.add(class_names)
    data = {
        # 'name' : name,
        'name_list' : lst,
    }
    return render(request, "Classroom.html", data)
