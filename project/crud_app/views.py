from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
@login_required(login_url='login_url')
def add_student(request):
    template_name = 'crud_app/add.html'
    form = StudentForm()
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name,context)
@login_required(login_url='login_url')
def show_student(request):
    template_name = 'crud_app/show.html'
    students = Student.objects.all()
    context = {'students': students}
    return render(request, template_name,context)
def update_student(request, pk):
    template_name = 'crud_app/add.html'
    obj = Student.objects.get(roll=pk)
    form = StudentForm(instance=obj)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name,context)
def delete_student(request, pk):
    template_name = 'crud_app/confirm.html'
    obj = Student.objects.get(roll=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, template_name)