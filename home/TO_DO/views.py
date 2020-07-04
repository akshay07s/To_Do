from django.shortcuts import render
from .models import To_Do
from django.utils import timezone

# Create your views here.
t = To_Do(data='Django is well running', timeStamp=timezone.now())
t.save()


def to_do(request):
    data_for_frontend={
    }
    return render(request, 'to_do/todo.html',data_for_frontend)
