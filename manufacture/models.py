from django.db import models


class Sales:
    vendor_code = models.CharField(max_length=40)
    # image = models.ImageField()
    type = models.CharField(max_length=40)
    size = models.CharField(max_length=40)
    pair = models.IntegerField()
    price = models.DecimalField(default=0.0)
    STATUSES = [
        ('Новый', 'Новый'),
        ('В процессе', 'В процессе'),
        ('Собран', 'Собран'),
        ('Отгружен', 'Отгружен'),
        ('Оплачен', 'Оплачен'),
    ]
    status = models.CharField(max_length=40, choices=STATUSES)
    total = models.DecimalField()
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f'{self.vendor_code}'
