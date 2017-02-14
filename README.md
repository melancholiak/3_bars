# Ближайшие бары

На сайте data.mos.ru есть много разных данных, в том числе список московских баров. Его можно скачать в формате json.
Требуется написать скрипт, который рассчитает:

    самый большой бар;
    самый маленький бар;
    самый близкий бар (текущие gps-координаты ввести с клавиатуры).


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и файла с входными данными формата json, с именем data.

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python
# затем появляются приглашения ввода координат.
# Вывод в терминал:
 biggest bar(s): Спорт бар «Красная машина», with amount of seats of 450
 smallest bar(s): БАР. СОКИ,Соки,Фреш-бар,Бар в Деловом центре Яуза,with amount of seats of 0 #ктото забил на подсчет мест
 nearest bar(s): Staropramen, with distance from u of 65.09729941317048
```
Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
