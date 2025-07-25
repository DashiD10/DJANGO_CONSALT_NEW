from django.shortcuts import render, HttpResponse
from .data import orders


def landing(request):
    return HttpResponse("<h1>Главная страница</h1>")


def thanks(request):
    return render(request, "thanks.html")


def orders_list(request):
    return HttpResponse("<h1>Список заказов</h1>")


def order_detail(request, order_id):
    """
    Отвечает за маршрут 'orders/<int:order_id>/'
    :param request: HttpRequest
    :param order_id: int (номер заказа)
    """
    order = [order for order in orders if order["id"] == order_id]
    try:
        order = order[0]
        context = {
            "order": order,
            "my_variable": "Hello, World!",
        }

    except IndexError:
        return HttpResponse("<h1>Заказ не найден</h1>", status=404)

    else:
        return render(request, "order_detail.html", context=context)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_my_name(self):
        return f"Меня зовут {self.name}"

    def __str__(self):
        return f"Это метод __str__: {self.name}"


test_list = ["Алевтина", "Бородач", "Гендальф Серый", "Лысый из Игры Престолов"]
test_dict = {"master": "Алевтина", "age": 25, "is_master": True}

test_person = Person("Лысый из Игры Престолов", 50)

def test_template(request):
    
    context_data = {
        "variable_1": "Значение переменной 1",
        "test_list": test_list,
        "test_dict": test_dict,
        "test_person": test_person,
    }
    return render(request, "test_template.html", context=context_data)
