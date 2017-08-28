import markdown
from django.views.generic import ListView, FormView, TemplateView, CreateView
from django.shortcuts import render, resolve_url
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .models import CurTime, Curator, Student, StudentGroup, CurTimeResult
from .forms import CurResultForm
import markdown
import json
import uuid


def create_notification(user=None, message='', *is_group, object_type):
    pass


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


class GroupAdd (TemplateView):
    model = Student
    template_name = "group.add.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['student_groups'] = StudentGroup.objects.all()
        return context


@require_POST
def save_students(request):
    students = request.POST.getlist('students[]')
    group_id = request.POST.get('group_id')

    if not students or not group_id:
        return JsonResponse({
            'error': 'Вы попытались сохранить пустые данные',
            'status': 'error'
        })

    for student in students:
        student = json.loads(student)
        new_student = Student.objects.create(
            group_id=group_id,
            first_name=student['first_name'],
            last_name=student['last_name'],
            phone=student['phone']
        )
        new_student.save()

    return JsonResponse({
        'status': 'OK'
    })


@require_GET
def list_students(request):
    group_id = request.GET.get('group_id')

    group_id = uuid.UUID(group_id)

    students = list(Student.objects.filter(group_id=group_id).values())

    return JsonResponse({
        'status': 'OK',
        'data': students
    })


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
    model = CurTimeResult
    form_class = CurResultForm
    template_name = "curs.done.html"

    def get_initial(self):
        return {
            'group': StudentGroup.objects.get(curator__user=self.request.user),
            'cur_time': self.kwargs['curs']
        }

    def get_success_url(self):
        return reverse('curs')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        students_count = Student.objects.filter(group__curator__user=self.request.user).count()
        context['students_count'] = range(1,students_count+1)
        return context


@login_required(login_url='/')
def get_rating(request):
    context = {}
    context['curators'] = Curator.objects.all()
    return render(request, 'rating.html', context=context)