
# Django REST Framework CRUD API

A robust Django REST Framework (DRF) project for managing a collection of books. This API supports **CRUD operations**, **pagination**, **filtering**, **search functionality**, and **JWT-based authentication**.

---

## Features

- **CRUD Operations**: Create, Read, Update, Delete books.
- **Authentication**: Token-based authentication using JWT.
- **Pagination**: Default pagination with 5 items per page.
- **Search and Filter**: Search by title/author and filter by author or publication date.
- **Error Handling**: Robust error responses for invalid requests.

---

## Tech Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: SQLite (default, can be switched to PostgreSQL/MySQL)
- **Authentication**: JSON Web Tokens (JWT)

---

## Installation

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/django-crud-api.git
cd django-crud-api
```

### 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

---

## API Endpoints

### Authentication
- **Obtain Tokens**: `POST /api/token/`  
  Request Body:
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```
  Response:
  ```json
  {
      "refresh": "your_refresh_token",
      "access": "your_access_token"
  }
  ```
- **Refresh Token**: `POST /api/token/refresh/`

---

### CRUD Endpoints

- **List All Books**: `GET /api/books/`  
  Optional query parameters:
  - `?search=title` - Search books by title/author.
  - `?author=John` - Filter books by author.
  - `?ordering=title` - Sort books by title.

- **Retrieve a Book**: `GET /api/books/<id>/`

- **Create a Book**: `POST /api/books/`  
  Request Body:
  ```json
  {
      "title": "Django for Beginners",
      "author": "William S. Vincent",
      "published_date": "2021-09-15",
      "isbn": "1234567890123"
  }
  ```

- **Update a Book**: `PUT /api/books/<id>/`  
  Request Body:
  ```json
  {
      "title": "Updated Title",
      "author": "Updated Author",
      "published_date": "2022-01-01",
      "isbn": "1234567890123"
  }
  ```

- **Delete a Book**: `DELETE /api/books/<id>/`

---

## Project Configuration

### Settings

- JWT Token Lifetimes:
  Adjust token lifetimes in `settings.py`:
  ```python
  SIMPLE_JWT = {
      'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
      'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
  }
  ```

- Pagination:
  Default page size is set to 5 in `settings.py`:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
      'PAGE_SIZE': 5,
  }
  ```

---

## Testing the API

### Using Postman
1. Obtain an `access` token by sending a `POST` request to `/api/token/`.
2. Use the token in the `Authorization` header for subsequent requests:
   ```
   Authorization: Bearer your_access_token
   ```

---

## Contribution

Contributions are welcome! If you find bugs or want to add new features:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add some feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---


## Contact

- **Author**: Musfiqur Rahman  
- **Email**: musfiqurrahmansayed@gmail.com 
- **GitHub**: [musfiqur552608](https://github.com/musfiqur552608)
