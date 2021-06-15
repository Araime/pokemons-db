# Карта покемонов

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/)

### Предметная область

Сайт для помощи по игре [Pokemon GO](https://www.pokemongo.com/en-us/). Это игра 
про ловлю [покемонов](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD).

Суть игры в том, что на карте периодически появляются покемоны, на определённый 
промежуток времени. Каждый игрок может поймать себе покемона, и пополнить свою 
личную коллекцию.

На карте может быть сразу несколько особей одного и того же покемона: например, 
3 Бульбазавра. Каждую особь могут поймать сразу несколько игроков. Если игрок 
поймал себе особь покемона, она исчезает для него, но остаётся для других.

В игре есть механика эволюции. Покемон одного вида может "эволюционировать" в 
другого. Так, например, Бульбазавр превращается в Ивизавра, а тот превращается в 
Венузавра.

![bulba evolution](https://dvmn.org/filer/canonical/1562265973/167/)

### Как установить

#### Скачать

Python3 должен быть уже установлен. Скачать этот репозиторий себе на компьютер.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

#### Быстрая настройка venv

Начиная с Python версии 3.3 виртуальное окружение идёт в комплекте в виде модуля
venv. Чтобы его установить и активировать нужно выполнить следующие действия в
командной строке:  

Указать скачанный репозиторий в качестве каталога.
```
cd C:\Users\ваш_пользователь\Downloads\папка_репозитория
```
Установить виртуальное окружение в выбранном каталоге.
```
Python -m venv env
```
В репозитории появится папка виртуального окружения env  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Hn4C6PD/image.png" alt="image" border="0"></a>

Активировать виртуальное окружение.
```
env\scripts\activate
```
Если всё сделано правильно, вы увидите в командной строке (env) слева от пути 
каталога.  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/MZ72r22/2.png" alt="2" border="0"></a>

### Как запустить

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки 
зависимостей:
```sh
pip install -r requirements.txt
```
Создайте БД:
```sh
python manage.py migrate
```
Создайте учетную запись администратора:
```sh
python manage.py createsuperuser
```
Запустите сервер разработки:
```sh
python manage.py runserver
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, 
создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: 
`ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в 
  случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

### Панель администратора

Для добавления новых покемонов, а также добавления их на карту, необходимо зайти
по адресу `адрес сервера/admin`. Для входа используйте учетную запись, созданную 
при помощи команды `createsuperuser`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на 
сайте [Devman](https://dvmn.org).