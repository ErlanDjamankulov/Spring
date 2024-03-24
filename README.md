# Django REST Project
Этот проект представляет собой простое приложение на Django, которое предоставляет API для управления компаниями и их продуктами,
контейнеризированное с помощью Docker Compose. Он включает в себя базу данных PostgreSQL и веб-сервер Django, что делает легким запуск и развертывание приложения на любой платформе поддерживающей Docker.
## Установка
1. Клонируйте репозиторий:

    git clone https://github.com/ErlanDjamankulov/Spring/
1.2 Убедитесь, что у вас установлены следующие инструменты:
- Docker
- Docker Compose
    
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
7. Сборка образов Docker
Выполните команду:

docker-compose build

Запуск контейнеров
Выполните команду:

docker-compose up

Остановка контейнеров
Когда закончите работу с приложением, выполните команду:

docker-compose down
    

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
