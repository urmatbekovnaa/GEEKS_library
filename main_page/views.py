from django.contrib import admin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from datetime import datetime

def books_list_view(request):
    if request.method == 'GET':
        books_list = models.Books.objects.filter().order_by('-id')
        context = {'books_list': books_list}
        return render(request, template_name='book.html', context=context)

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)

def page_about_me(request):
    if request.method == "GET":
        return HttpResponse('<h1>ЗДРАВСТВУЙТЕ, меня зовут Адина.</h1>'
                            '<p>Я 2007 года рождения, ученица 10-го класса.</p>'
                            '<p>Я студентка GEEKS academy. Учусь на Backend разработчика уже четвертый месяц.</p>')

def about_my_pets(request):
    if request.method == "GET":
        return HttpResponse('<p>Мое любимое животное это - кошки.<p>'
                            '<p>Изначально, я не питала особую симпатию к кошкам, но со временем это изменилось, <p>'
                            '<p>и теперь я очень люблю их.</p>'
                            '<p><img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcYPMFW3Z1zG9D7GOU7p_GJYrkfbMpsGdXjA&s><p> ')

def system_time(request):
    current_time = datetime.now()
    return HttpResponse(f"Current system date and time: {current_time}")
