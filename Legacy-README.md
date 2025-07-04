# Apartment Rental Service

## Технологічний стек

### Backend

- **Python 3.10+** з type hints
- **Django 4.2** + **Django Rest Framework (DRF)**
- **PostgreSQL** для бази даних
- **JWT** для автентифікації користувачів
- **DRF Spectacular** для автоматичної документації API
- **Docker** + **Docker Compose** для контейнеризації

### Frontend

- **Vue.js 3** (Composition API)
- **Vue Router** для навігації
- **Tailwind CSS 3**
- **Axios** для HTTP запитів
- **Vite** для збірки проекту

---

## Вимоги до завдання

### Part 1: Backend завдання

#### 1. Створення моделі **Apartment**

Необхідно створити модель **Apartment** з наступними полями:

- `name` — максимальна довжина 100 символів
- `slug` — унікальний ідентифікатор
- `description` — опис квартири
- `price` — ціна, тип decimal, максимальна кількість цифр 8, з двома десятковими знаками
- `number_of_rooms` — кількість кімнат
- `square` — площа в квадратних метрах, тип decimal
- `availability` — доступність (boolean)
- `owner` — зовнішній ключ до моделі користувача
- `created_at`, `updated_at` — дати створення та останнього оновлення

Додати модель до Django Admin панелі з можливістю фільтрації та пошуку по ключових полях.

#### 2. Реалізація API Endpoints

- **GET /api/v1/apartments/**  
  Список всіх квартир з фільтрами:
  - `price_min`
  - `price_max`
  - `rooms`
  - `available`
  - `search` (за назвою або описом)
  - Пагінація (10 елементів на сторінку)
  - Доступ для всіх користувачів (allow any)
- **GET /api/v1/apartments/{slug}/**  
  Деталі квартири за `slug`.

- **POST /api/v1/apartments/**  
  Створення нової квартири (доступно тільки для авторизованих користувачів).

- **PUT/DELETE /api/v1/apartments/{slug}/**  
  Редагування/видалення квартири (доступно тільки для власника квартири).

Додати документацію для цих endpoints за допомогою **drf-spectacular** (`/api/v1/docs/`).

#### 3. ✨ Додатково

- Створити скрипт для автоматичного додавання кількох користувачів та квартир (з використанням **Factory Boy** та Django команд).

### Part 2: Frontend завдання

#### 1. Створення сторінок

- **Сторінка зі списком квартир**:
  - Пагінація та фільтри:
    - Ціна, кількість кімнат, доступність, пошук за назвою або описом.
  - Кожен елемент списку має бути посиланням на деталі квартири.
- **Сторінка детальної інформації про квартиру**:
  - Відображення всіх полів моделі **Apartment**.

#### 2. Дизайн

- Використовувати **Vue.js** (за бажанням - React) та **TailwindCSS** для побудови інтерфейсу.
- Дизайн має бути адаптивним, працювати як на десктопах, так і на мобільних пристроях.
- Якщо квартира недоступна, візуально відображати це через зміни в стилях (наприклад, зниження непрозорості або застосування ефекту blur).

#### 3. Запити до Backend

- Для запитів до Backend використовувати **Axios**, при цьому базовий URL буде зберігатися в змінній середовища **VITE_API_URL**.

#### 4. ✨ Додатково

- Реалізувати сторінку **Login**:

  - Валідація форми.
  - Запит на авторизацію в Backend.
  - Зберігання отриманого токену.

- Всі сторінки повинні бути інтегровані з Backend, реалізувати сторінку для логіну з відповідною обробкою токенів.

---

## Запуск проекту

Щоб запустити проект, скористайтеся наступними командами:

```bash
docker compose build
docker compose up
```

---

## Послідовність дій

1. Клонуйте цей репозиторій на свій локальний комп'ютер.
2. Запустіть проект за допомогою docker compose. Проект уже налаштований для роботи в середовищі розробки (dev).
3. Виконайте завдання, зазначені в частинах Part 1 та Part 2.
4. Завантажте код до власного репозиторію на GitHub у режимі private і додайте користувача mvk-mash у список колабораторів (Collaborators).
