import json
from account.models import Account
from django.utils.timezone import zones as timezone_zones

timezone_list = []

# Загрузка JSON таблицы
with open('Russian-Regions-And-Cities-With-Time-Zone.json', 'r') as f:
    data = json.load(f)

# Обработка данных и создание списка выбора
for item in data:
    cities = item['cities']
    for city in cities:
        timezone = city['time_zons']
        timezone_name = timezone_zones[timezone]
        timezone_list.append((timezone, timezone_name))

# Добавление списка выбора в модель Account
Account._meta.get_field('time').choices = timezone_list
