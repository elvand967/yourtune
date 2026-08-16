"""
Конфигурация URL-адресов для проекта конфигурации.

Список `urlpatterns` направляет URL-адреса к представлениям. Для получения дополнительной информации см.:

https://docs.djangoproject.com/en/5.2/topics/http/urls/
Примеры:
Представления на основе функций
1. Добавьте импорт: from my_app import views

2. Добавьте URL-адрес в urlpatterns: path('', views.home, name='home')
Представления на основе классов

1. Добавьте импорт: from other_app.views import Home

2. Добавьте URL-адрес в urlpatterns: path('', Home.as_view(), name='home')
Включение еще одного URLconf

1. Импортируйте функцию include(): from django.urls import include, path

2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
