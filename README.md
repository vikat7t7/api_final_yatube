# API Yatube

Этот проект представляет собой REST API для социальной сети Yatube.  API предоставляет функциональность для взаимодействия с данными пользователей и их подписками.  Он разработан на основе фреймворка Django REST Framework и использует JWT для аутентификации.

## Описание

API Yatube позволяет разработчикам взаимодействовать с основными функциями социальной сети, такими как управление подписками на других пользователей.  API спроектирован с использованием архитектуры REST и предоставляет хорошо документированные эндпоинты для различных операций.  Он обеспечивает безопасность данных пользователей с помощью JWT-аутентификации и контролирует доступ на основе ролей.

## Установка

1. Клонирование репозитория:
   
   git clone <ссылка_на_репозиторий>
   
2. Создание и активация виртуального окружения:
   
   python3 -m venv venv
   source venv/bin/activate
   
3. Установка пакетов:
   
   pip install -r requirements.txt
   
4. Миграции:
   
   python manage.py migrate
   
5. Запуск сервера:
   
   python manage.py runser
