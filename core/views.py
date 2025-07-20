from django.shortcuts import render, HttpResponse

def landing(request): 
    return HttpResponse("<h1>Главная страница</h1>")

def thanks(request):
    return HttpResponse("<h1>Спасибо за заказ!</h1>")

def orders_list(request):
    return HttpResponse("<h1>Список заказов</h1>")

def order_detail(request):
    return HttpResponse("<h1>Детали заказа</h1>")

# Create your views here.
