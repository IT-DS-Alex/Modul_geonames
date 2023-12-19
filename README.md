# Описание проекта

## Цель:
Сопоставление произвольных гео названий с унифицированными именами geonames для внутреннего использования Карьерным центром
## Задачи:
Создать решение для подбора наиболее подходящих названий с geonames. Например Ереван -> Yerevan

На примере РФ и стран наиболее популярных для релокации - Беларусь, Армения, Казахстан, Кыргызстан, Турция, Сербия. Города с населением от 15000 человек (с возможностью масштабирования на сервере заказчика)

Возвращаемые поля geonameid, name, region, country, cosine similarity

формат данных на выходе: список словарей, например [{dict_1}, {dict_2}, …. {dict_n}] где словарь - одна запись с указанными полями

### Описание данных
#### Используемые таблицы с geonames:

admin1CodesASCII

alternateNamesV2

cities15000

countryInfo

#### Дополнительно:

при необходимости любые другие открытые данные

таблицы geonames можно скачать здесь http://download.geonames.org/export/dump/

Тестовый датасет: https://disk.yandex.ru/d/wC296Rj3Yso2AQ

## Настройка базы данных MySQL из данных GeoNames:

простой скрипт для создания базы данных GeoNames для потребностей заказчика.

Скачиваем и распаковываем необходимые данные в соответствии с требованием заказчика:

http://download.geonames.org/export/dump/admin1CodesASCII.zip

http://download.geonames.org/export/dump/alternateNamesV2.zip

http://download.geonames.org/export/dump/cities15000.zip

http://download.geonames.org/export/dump/countryInfo.zip
