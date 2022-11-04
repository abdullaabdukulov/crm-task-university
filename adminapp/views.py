from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')


@login_required_decorator
def home_page(request):
    faculties = services.get_faculty()
    kafedras = services.get_kafedra()
    subjects = services.get_subject()
    teachers = services.get_teacher()
    groups = services.get_group()
    students = services.get_student()
    ctx = {
        'counts': {
            'faculties': len(faculties),
            'kafedras': len(kafedras),
            'subjects': len(subjects),
            'teachers': len(teachers),
            'groups': len(groups),
            'students': len(students),

        },
        "groups": {
            "student": students,
        }
    }
    return render(request, 'index.html', ctx)


@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect('faculty_list')


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculty()
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, 'faculty/list.html', ctx)


# KAFEDRA
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = Kafedra_Form(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = Kafedra_Form(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('kafedra_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect('kafedra_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedra()
    ctx = {
        "kafedras": kafedras
    }
    return render(request, 'kafedra/list.html', ctx)


@login_required_decorator
def subject_create(request):
    model = Subject()
    form = Subject_Form(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        'form': form,
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(pk=pk)
    form = Subject_Form(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_delete(request, pk):
    model = Subject.objects.get(pk=pk)
    model.delete()
    return redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_subject()
    ctx = {
        'subjects': subjects
    }
    print(subjects)
    return render(request, 'subject/list.html', ctx)


@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = Teacher_Form(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx = {
        'form': form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(pk=pk)
    form = Teacher_Form(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teacher.objects.get(pk=pk)
    model.delete()
    return redirect('teacher_list')


@login_required_decorator
def teacher_list(request):
    teachers = services.get_teacher()
    ctx = {
        'teachers': teachers
    }

    print(ctx)
    return render(request, 'teacher/list.html', ctx)


@login_required_decorator
def group_create(request):
    model = Group()
    form = Group_Form(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {
        'form': form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(pk=pk)
    form = Group_Form(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
    ctx = {
        'form': form,
        'model': model
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_delete(request, pk):
    model = Group.objects.get(pk=pk)
    model.delete()
    return redirect('group_list')


@login_required_decorator
def group_list(request):
    groups = services.get_group()
    ctx = {
        'groups': groups
    }
    return render(request, 'group/list.html', ctx)


@login_required_decorator
def student_create(request):
    model = Student()
    form = Student_Form(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        'form': form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_edit(request, pk):
    model = Student.objects.get(pk=pk)
    form = Student_Form(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_delete(request, pk):
    model = Student.objects.get(pk=pk)
    model.delete()
    return redirect('student_list')


@login_required_decorator
def student_list(request):
    students = services.get_student()
    ctx = {
        'students': students
    }
    print(ctx)
    return render(request, 'student/list.html', ctx)


