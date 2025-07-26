"""
URL configuration for barbershop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

### Таблица маршрутов, представлений и шаблонов

"""
| Маршрут                     | Представление        | Шаблон                     | Псевдоним маршрута |
| --------------------------- | -------------------- | -------------------------- | ------------------ |
| `'/'`                       | `views.landing`      | `./landing.html`           | `landing`          |
| `'/thanks/'`                | `views.thanks`       | `./core/thanks.html`       | `thanks`           |
| `'/orders/'`                | `views.orders_list`  | `./core/orders_list.html`  | `orders_list`      |
| `'/orders/<int:order_id>/'` | `views.order_detail` | `./core/order_detail.html` | `order_detail`     |
"""

from django.contrib import admin
from django.urls import path
from core.views import landing, thanks, orders_list, order_detail, orders_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing),
    path("thanks/", thanks),
    path("orders/", orders_list),
    path("orders/<int:order_id>/", order_detail),
]
