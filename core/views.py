from django.shortcuts import render, HttpResponse
from .data import orders


def landing(request):
    return HttpResponse("<h1>Главная страница</h1>")


def thanks(request):
    return render(request, "thanks.html")


def orders_list(request):
    context = {
        "orders": orders,
    }
    return render(request, "orders_list.html", context=context)


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


