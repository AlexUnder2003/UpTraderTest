# Django Tree Menu

Это Django-приложение реализует **древовидное меню**, тестовое задание UpTrader.

---

## 📦 Установка

1. Клонируйте репозиторий или скопируйте приложение `menu` в ваш Django-проект:

```

your\_project/
├── menu/
├── templates/
├── static/
├── your\_app/
└── manage.py

````

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate   # для Linux/macOS
venv\Scripts\activate      # для Windows
````

3. Установите зависимости:

```bash
pip install -r requirements.txt
```


4. Подключите приложение в `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'menu',
]
```

5. Примените миграции:

```bash
python manage.py makemigrations menu
python manage.py migrate
```

6. (опционально) Загрузите пример фикстуры:

```bash
python manage.py loaddata fixture.json
```

---

## 🛠 Использование

1. В админке создайте меню (`Menu`) и добавьте вложенные пункты (`MenuItem`).

2. Для ссылки можно указать:

   * `named_url` (имя URL из `urls.py`)
   * или прямой `url` (`/about/`, `/contacts/` и т.д.)

3. В шаблоне подключите тег и вызовите отрисовку:

```django
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```

---

## ✨ Поведение

* Активный пункт определяется по `request.path` и подсвечивается
* Все его родительские ветки автоматически раскрываются
* Используется Bootstrap 5 + кастомные стили
* Меню вертикальное, с кнопками раскрытия подменю
* Раскрытие реализовано через Bootstrap Collapse

---

## 📁 Структура меню

Пример:

```
О нас
├── Команда
│   └── Карьера
└── История
```

---

## 👤 Автор

**Назимов Александр**
