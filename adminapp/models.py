import django.db.models.deletion
from django.db import models


class Faculty(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    kafedra = models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminapp.Kafedra')
    subject = models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminapp.Subject')
    image = models.ImageField(upload_to='teachers', null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminapp.Faculty')

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
