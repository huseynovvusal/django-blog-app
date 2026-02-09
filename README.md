# Django Blog Application 🚀

A professional, modularized Django-based blog application featuring **JWT authentication with HttpOnly cookies**, a custom user model, and a robust architecture. This project is built with modern practices using Django 5.0 and Django REST Framework.

## 🌟 Key Features

- **Custom User Model**: Extended user management using a dedicated `users` app.
- **JWT Authentication**: Secure authentication system using `rest_framework_simplejwt` with a custom middleware for HttpOnly cookie management.
- **Modular Architecture**: Clean separation of concerns with apps logic located in the `apps/` directory.
- **Base Model Utility**: Shared model attributes (UUID, timestamps) across all entities through an abstract `BaseModel`.
- **PostgreSQL Ready**: Pre-configured for PostgreSQL with Docker support for the database layer.
- **Pagination**: Consistent API and web pagination handled via common utilities.

## 🛠 Tech Stack

- **Framework**: [Django 5.0](https://www.djangoproject.com/)
- **API Engine**: [Django REST Framework](https://www.django-rest-framework.org/)
- **Authentication**: [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **Environment**: [Django Environ](https://django-environ.readthedocs.io/)
- **Containerization**: [Docker](https://www.docker.com/) & Docker Compose

## 🏗 Project Structure

```text
├── apps/
│   ├── authentication/  # JWT & Cookie-based auth logic
│   ├── blog/            # Core blog functionality (Posts, Slugs)
│   ├── common/          # Shared models (BaseModel), pagination, etc.
│   └── users/           # Custom User model and management
├── config/              # Project settings and root URL configurations
├── docker/              # Docker configurations
│   ├── local/           # Development Dockerfile
│   └── production/      # Production Dockerfile
├── requirements/        # Base and local dependency management
├── templates/           # HTML templates for frontend views
└── manage.py            # Django management CLI
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (recommended)
- PostgreSQL (if running locally without Docker)

### Quick Start with Docker (Recommended)

#### Development Environment

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd django-blog-app
   ```

2. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   POSTGRES_DB=blog_db
   POSTGRES_USER=blog_user
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```

3. **Build and Start Services**:
   ```bash
   docker-compose up --build
   ```

4. **Run Migrations** (in a new terminal):
   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Access the Application**:
   - Web: `http://localhost:8000`
   - Admin: `http://localhost:8000/admin`

#### Production Environment

1. **Configure Production Environment**:
   Create a `.env.docker` file with production settings:
   ```env
   POSTGRES_DB=blog_db
   POSTGRES_USER=blog_user
   POSTGRES_PASSWORD=secure_production_password
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   DEBUG=False
   SECRET_KEY=your_production_secret_key
   ```

2. **Build and Deploy**:
   ```bash
   docker-compose -f docker-compose.prod.yml up --build -d
   ```

3. **Run Production Setup**:
   ```bash
   docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
   docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
   docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
   ```

### Local Development (Without Docker)

1. **Install Dependencies**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements/local.txt
   ```

2. **Setup PostgreSQL** and configure `.env` with `POSTGRES_HOST=localhost`

3. **Run Migrations & Start Server**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

## 🔐 Authentication Mechanism

This project implements a secure **JWT-in-Cookie** authentication flow:
- Access and Refresh tokens are stored in `HttpOnly` and `SameSite` cookies.
- A custom `JWTAuthMiddleware` automatically handles token extraction and validation from these cookies.
- Automatic token refreshing is handled transparently by the middleware if a valid refresh token exists.

## 📝 Workflow

- **Create Superuser**: `python manage.py createsuperuser`
- **Create Migrations**: `python manage.py makemigrations`
- **Run Tests**: `python manage.py test`

---
*Professional documentation generated for the Django Blog App project.*
