# Locallibrary Django Mini app

Проект LocalLibrary — это веб-приложение на базе Django, предназначенное для управления и отображения информации о книгах, авторах и процессах выдачи книг. Приложение предоставляет функционал для просмотра книг и авторов, проверки списка взятых книг, продления сроков возврата книг (для библиотекарей), а также выполнения операций CRUD (создание, чтение, обновление, удаление) для книг и авторов.

Этот файл README содержит обзор структуры проекта, его функциональности и инструкции по развертыванию.
---

## Описание проекта

1. **Главная страница** (`/catalog/`) - отображает общую статистику библиотеки: количество книг, экземпляров книг, доступных экземпляров и авторов.
   - Счетчик посещений для отслеживания числа посещений пользователем главной страницы.
2. **Список всех книг** (`/catalog/books`) - просмотр списка всех книг с пагинацией.
3. **Детальная информация о книге** (`/catalog/book/<int:pk>/`) - просмотр детальной информации о книге.
4. **Создание, обновление и удаление книги**:
   - Создание: `/catalog/book/create`
   - Обновление: `/catalog/book/<int:pk>/update`
   - Удаление: `/catalog/book/<int:pk>/delete`
5. **Список книг, взятых их библиотеки пользователем** (`/catalog/mybooks/`) - просмотр списка книг, взятых из библиотеки пользователем
6. **Список книг, взятых их библиотеки** (`/catalog/borrowed/`) - просмотр списка книг, взятых из библиотеки
7. **Продлевает дата возврата книги** (`/catalog/book/<uuid:pk>/renew/`) - для продления даты возврата книги
8. **Список всех авторов** (`/catalog/authors`) - просмотр списка всех авторов.
3. **Детальная информация об авторе** (`/catalog/authors/<int:pk>/`) - просмотр детальной информации об авторе.
4. **Создание, обновление и удаление автора**:
   - Создание: `/catalog/authors/create`
   - Обновление: `/catalog/authors/<int:pk>/update`
   - Удаление: `/catalog/authors/<int:pk>/delete`

Проект также развернут с использованием Docker для удобства развертывания.

---

## Требования

Для запуска проекта вам понадобится:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.9+ (если вы хотите запустить проект локально без Docker)

---

## Установка и запуск

### 1. Клонирование репозитория

Склонируйте репозиторий на ваш компьютер:

```bash
git clone https://github.com/Mefistop/django_locallibrary.git
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта и добавьте следующие переменные окружения:

```env
DJANGO_LOGLEVEL
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=
DB_NAME=blog_db
DB_USER=blog_user
DB_PASSWORD=blog_password
DB_HOST=db
DB_PORT=5432
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=adminpassword
DJANGO_SUPERUSER_EMAIL=admin@example.com
```
Замените your-secret-key на случайную строку (например, используйте Django Secret Key Generator ).

### 3. Запуск с помощью Docker

Если у вас установлен Docker, выполните следующие команды:

```bash
docker compose up --build
```

Это создаст и запустит контейнеры для Django, PostgreSQL. После завершения сборки проект будет доступен по адресу:
```env
http://localhost:8000/
```

**Автоматические миграции и создание суперпользователя**

**Во время запуска Docker автоматически выполняет следующие действия**:

- Применяет миграции базы данных.
- Создает суперпользователя (если он еще не существует) с данными, указанными в переменных окружения:
  - `DJANGO_SUPERUSER_USERNAME`
  - `DJANGO_SUPERUSER_PASSWORD`
  - `DJANGO_SUPERUSER_EMAIL` (опционально)
- Собирает статические файлы.



## Использование проекта

### Админка

Админка доступна по адресу:
```env
http://localhost:8000/admin/
```

Используйте учетные данные суперпользователя для входа.

---

### Создание постов и авторов

- Войдите в админку.
- Создайте авторов книг (`Author`).
- Создайте жанры книг (`Genre`).
- Создайте языки книг (`Language`).
- Создайте книги (`Book`).
- Создайте экземпляры книг (`BookInstance`).

---

### Просмотр библиотеки

- Главная страница: `http://localhost:8000/catalog/`
- Список книг: `http://localhost:8000/catalog/books/`
- Список авторов: `http://localhost:8000/catalog/authors/`
- Детальная страница книги: `http://localhost:8000/catalog/book/<int:pk>/`
- Страница автора: `http://localhost:8000/catalog/author/<int:pk>/`
- Список книг, взятых их библиотеки пользователем: `http://localhost:8000/catalog/mybooks/`
- Список всех книг, взятых их библиотеки:`http://localhost:8000/catalog/borrowed/`



4. **Создание, обновление и удаление автора**:
   - Создание: `/catalog/authors/create`
   - Обновление: `/catalog/authors/<int:pk>/update`
   - Удаление: `/catalog/authors/<int:pk>/delete`
---

### Создание, обновление и удаление книг

- Создание новой книги: `http://localhost:8000/catalog/book/create/`
- Обновление книги: `http://localhost:8000/catalog/book/<int:pk>/update/`
- Удаление книги: `http://localhost:8000/catalog/book/<int:pk>/delete/`
- Продление книги: `http://localhost:8000/catalog/book/<uuid:pk>/renew/`

---

### Создание, обновление и удаление автора

- Создание нового автора: `http://localhost:8000/catalog/authors/create/`
- Обновление автора: `http://localhost:8000/catalog/authors/<int:pk>/update/`
- Удаление автора: `http://localhost:8000/catalog/authors/<int:pk>/delete/`

---

### Тестирование

Для запуска тестов выполните следующую команду:

```bash
docker-compose exec web python manage.py test
```
Тесты проверяют основные функции проекта, включая:

- Отображение страниц.
- Пагинацию.
- Формы комментариев.
- Аутентификацию.

# Запуск без Docker

Если вы хотите запустить проект локально без Docker, выполните следующие шаги:

1. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```
2. **Создайте базу данных PostgreSQL и настройте подключение в `settings.py`**
3. **Примените миграции:**
   ```bash
   python manage.py migrate
   ```
4. **Создайте суперпользователя:**
   ```bash
   python manage.py createsuperuser
   ```
5. **Соберите статические файлы:**
   ```bash
   python manage.py collectstatic
   ```
6. **Запустите сервер разработки:**
   ```bash
   python manage.py runserver
   ```

## Автор
Этот проект был создан как часть учебного проекта по Django.