from django.contrib import admin
from .models import Advertisement  # импортирую свою модель
# класс объекта
from django.db.models.query import QuerySet


# py manage.py createuser - создание аккаунта супер пользователя
# http://127.0.0.1:8000/admin


# класс для кастомизации модели в админке
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'updated_date']
    list_filter = ['auction', 'created_at', 'price']  # столбцы по которым будет фильтрация
    actions = ['make_auction_as_false', 'make_auction_as_true']  # методы для выбранных записей
    fieldsets = (
        ('Общие', {  # блок 1
            "fields": (
                'title', 'description'  # поля блока
            ),
        }),
        ('Финансы', {  # блок 2
            "fields": (
                'price', 'auction'  # поля блока
            ),
            'classes': ['collapse'] # скрыть/показать блок
        })
    )


    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset: QuerySet):
        queryset.update(auction=True)

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset: QuerySet):
        queryset.update(auction=False)


# подключение модели в админку и кастомной модели
admin.site.register(Advertisement, AdvertisementAdmin)


"""def dec(func):
    def wrapper():
        print()
        func()
        print()

    return


def add_list(some_list: list):
    some_list
"""