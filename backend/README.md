# Skillcart Backend - Django REST Framework API

This is the backend API for the Skillcart e-commerce website, built with Django REST Framework and MySQL.

## Features

- RESTful API for products, categories, tags, and orders
- MySQL database integration
- Product management with images, pricing, and descriptions
- Order management system
- Site settings management
- CORS enabled for frontend integration
- Admin panel for content management

## Project Structure

```
backend/
├── manage.py
├── requirements.txt
├── skillcart_backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── api/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    └── urls.py
```

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- MySQL 5.7 or higher
- pip (Python package manager)

### 2. Create Virtual Environment

```bash
cd backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** If you encounter issues installing `mysqlclient`, you may need to install MySQL development libraries:

- **Windows:** Download MySQL Connector/C from MySQL website
- **Linux:** `sudo apt-get install default-libmysqlclient-dev` (Ubuntu/Debian)
- **Mac:** `brew install mysql-client`

Alternatively, you can use `pymysql` instead:

```bash
pip install pymysql
```

Then add this to `skillcart_backend/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### 4. Configure MySQL Database

1. Create a MySQL database:
```sql
CREATE DATABASE skillcart_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Update database settings in `skillcart_backend/settings.py` or set environment variables:
```bash
# Windows (PowerShell)
$env:DB_NAME="skillcart_db"
$env:DB_USER="root"
$env:DB_PASSWORD="your_password"
$env:DB_HOST="localhost"
$env:DB_PORT="3306"

# Linux/Mac
export DB_NAME=skillcart_db
export DB_USER=root
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_PORT=3306
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Load Initial Data (Optional)

You can create a management command or use Django admin to add initial products, categories, and settings.

### 8. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## API Endpoints

### Products

- `GET /api/products/` - List all products
- `GET /api/products/{id}/` - Get product details
- `GET /api/products/{slug}/` - Get product by slug
- `GET /api/products/featured/` - Get featured products
- `GET /api/products/by_price/?min_price=100&max_price=500` - Filter by price
- `GET /api/products/by_category/?category=slug` - Filter by category

**Query Parameters:**
- `search` - Search in name, description
- `category` - Filter by category ID
- `tags` - Filter by tag IDs
- `is_featured` - Filter featured products
- `ordering` - Order by field (e.g., `price`, `-created_at`)

### Categories

- `GET /api/categories/` - List all categories
- `GET /api/categories/{slug}/` - Get category details
- `GET /api/categories/{slug}/products/` - Get products in category

### Tags

- `GET /api/tags/` - List all tags
- `GET /api/tags/{slug}/` - Get tag details
- `GET /api/tags/{slug}/products/` - Get products with tag

### Orders

- `POST /api/orders/` - Create new order
- `GET /api/orders/{id}/` - Get order details
- `PATCH /api/orders/{id}/update_status/` - Update order status
- `GET /api/orders/by_email/?email=user@example.com` - Get orders by email

**Order Creation Example:**
```json
{
  "email": "customer@example.com",
  "phone": "1234567890",
  "customer_name": "John Doe",
  "product": 1,
  "quantity": 1,
  "bump_offer_added": false,
  "bump_offer_price": null
}
```

### Settings

- `GET /api/settings/` - Get site settings

## Admin Panel

Access the admin panel at `http://localhost:8000/admin/` using your superuser credentials.

You can manage:
- Products (add, edit, delete)
- Categories
- Tags
- Orders
- Site Settings

## Media Files

Uploaded product images will be stored in the `media/products/` directory. Make sure to configure your web server to serve media files in production.

## Production Deployment

Before deploying to production:

1. Change `DEBUG = False` in settings.py
2. Set a strong `SECRET_KEY`
3. Configure proper `ALLOWED_HOSTS`
4. Set up proper database credentials
5. Configure static file serving
6. Set up SSL/HTTPS
7. Restrict CORS origins
8. Use environment variables for sensitive data

## Environment Variables

Create a `.env` file (use `python-decouple` or similar):

```
DB_NAME=skillcart_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=your-secret-key-here
DEBUG=False
```

## Troubleshooting

### MySQL Connection Issues

- Ensure MySQL server is running
- Verify database credentials
- Check if MySQL port (3306) is accessible
- For Windows, ensure MySQL Connector/C is installed

### Migration Issues

- Delete migration files (except `__init__.py`) and run `makemigrations` again
- Ensure database exists and user has proper permissions

### Static Files Not Loading

- Run `python manage.py collectstatic`
- Configure web server to serve static files

## Support

For issues or questions, please check the Django and DRF documentation:
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)




