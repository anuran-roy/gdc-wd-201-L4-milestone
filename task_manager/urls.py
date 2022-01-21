from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

tasks_list = []
completed_list = []


def tasks(request):
    return render(request, "tasks.html", {"tasks": tasks_list})


def add_tasks(request):
    task = request.GET.get("task")
    tasks_list.append(task)

    return HttpResponseRedirect("/tasks")


def delete(request, index):
    del tasks_list[index - 1]
    return HttpResponseRedirect("/tasks")


def mark_as_done(request, index):
    task = tasks_list[index - 1]
    completed_list.append(str(task))

    del tasks_list[index - 1]

    return HttpResponseRedirect("/tasks")


def completed(request):
    return render(request, "completed.html", {"completed": completed_list})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", tasks),
    path("add-task/", add_tasks),
    path("delete-task/<int:index>/", delete),
    path("complete_task/<int:index>/", mark_as_done),
    path("completed_tasks/", completed)
    # Add all your views here
]
