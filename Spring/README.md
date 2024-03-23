# Django REST Project
Этот проект представляет собой простое приложение на Django, которое предоставляет API для управления компаниями и их продуктами.
## Установка
1. Клонируйте репозиторий:

    git clone https://github.com/ErlanDjamankulov/Spring/
    
2. Перейдите в директорию проекта:

    cd Spring2024

3. Создайте виртуальное окружение (рекомендуется):

    python -m venv venv

4. Активируйте виртуальное окружение:

    - Для Windows:
       
        venv\Scripts\activate  

    - Для macOS и Linux:
        
        source venv/bin/activate
        
5. Установите зависимости:
  
    pip install -r requirements.txt
    
6. Примените миграции:
   
    python manage.py migrate
    

## Использование

Для запуска сервера разработки Django, выполните следующую команду:

python manage.py runserver

После запуска сервера вы сможете получить доступ к API по следующим адресам:

Компании: http://127.0.0.1:8000/companies/
Продукты: http://127.0.0.1:8000/products/

Модели данных

Компания (Company)
Модель Company содержит следующие поля:

id: Первичный ключ компании (тип данных SmallIntegerField).
title: Название компании (тип данных CharField).
description: Описание компании (тип данных TextField).
location: Местоположение компании (тип данных CharField).
logo: Логотип компании (тип данных ImageField).
timetable: График работы компании (тип данных CharField).

Продукт (Product)
Модель Product содержит следующие поля:

title: Название продукта (тип данных CharField).
description: Описание продукта (тип данных TextField).
price: Цена продукта (тип данных PositiveIntegerField).
stock: Количество продукта на складе (тип данных PositiveIntegerField).
image: Изображение продукта (тип данных ImageField).
create_date: Дата создания продукта (тип данных DateTimeField).
company: Внешний ключ на компанию, к которой относится продукт (тип данных ForeignKey).

Автор: Джаманкулов Эрлан
