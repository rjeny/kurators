import markdown
from django.views.generic import ListView, FormView, TemplateView, CreateView
from django.shortcuts import render, resolve_url
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .models import CurTime, Curator, Student, StudentGroup
from .forms import CurResultForm
import markdown


class MainPage (ListView):
    template_name = 'index.html'
    model = Curator


class CuratorList (ListView):
    model = Curator
    template_name = "curator_list.html"


class CuratorAdd (CreateView):
    model = Curator
    template_name = "curator_add.html"
    fields = ['last_name', 'first_name', 'middle_name', 'groupName', 'email']

    def get_success_url(self):
        return reverse('curators')


class MyPage (TemplateView):
    template_name = "mypage.html"


class GroupList (ListView):
    model = Student
    template_name = "group_list.html"


class GroupsList (ListView):
    model = StudentGroup
    template_name = "groups_list.html"


class GroupsAdd (CreateView):
    model = StudentGroup
    template_name = "curator_add.html"
    fields = ['faculty', 'number', 'curator']

    def get_success_url(self):
        return reverse('groups')


class CursList (ListView):
    template_name = 'cur_list.html'
    model = CurTime


@login_required(login_url='/')
@require_GET
def get_curs_manual(request):
    id = request.GET.get('id')
    if id:
        manual = CurTime.objects.get(id=id).manual
        manual = markdown.markdown(str(manual))
    else:
        manual = "Инструкции нет"
    return HttpResponse(manual)


class CursResult (CreateView):
    form_class = CurResultForm


@login_required(login_url='/')
def get_rating(request):
    context = {}
    context['curators'] = Curator.objects.all()
    return render(request, 'rating.html', context=context)