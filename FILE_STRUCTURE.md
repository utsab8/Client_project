# File Structure - Django Organization

All files have been reorganized into Django's standard structure.

## 📁 Current Structure

```
skillcart/
├── backend/
│   ├── templates/              # HTML templates
│   │   ├── index.html         # Homepage
│   │   ├── product.html       # Product detail page
│   │   └── checkout.html      # Checkout page
│   │
│   ├── static/                 # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── style.css      # Main stylesheet
│   │   └── js/
│   │       ├── api.js         # API client
│   │       └── script.js      # Frontend scripts
│   │
│   ├── api/                    # Django app
│   │   ├── models.py          # Database models
│   │   ├── views.py           # API views
│   │   ├── views_frontend.py  # Frontend page views
│   │   ├── serializers.py    # API serializers
│   │   └── urls.py            # API URLs
│   │
│   ├── skillcart_backend/     # Django project
│   │   ├── settings.py        # Django settings
│   │   └── urls.py            # Main URL configuration
│   │
│   ├── manage.py
│   └── requirements.txt
│
└── (old directories removed)
```

## ✅ What Changed

### 1. **Templates** (`backend/templates/`)
- All HTML files moved here
- Use Django template tags: `{% load static %}`
- Static files referenced with: `{% static 'path' %}`

### 2. **Static Files** (`backend/static/`)
- CSS files in `backend/static/css/`
- JS files in `backend/static/js/`
- Served automatically by Django

### 3. **Django Views**
- Created `api/views_frontend.py` for frontend pages
- URLs configured in `skillcart_backend/urls.py`

## 🔧 Django Settings Updated

### Templates Configuration
```python
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],  # Points to backend/templates/
        ...
    },
]
```

### Static Files Configuration
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Points to backend/static/
]
```

## 🌐 URL Routing

- `/` → Homepage (`index.html`)
- `/product.html?slug=...` → Product page
- `/checkout.html?slug=...` → Checkout page
- `/api/...` → API endpoints
- `/admin/` → Django admin

## 📝 Using Static Files in Templates

All templates now use Django's static file system:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/api.js' %}"></script>
```

## 🚀 Running the Server

1. **Start Django server:**
   ```bash
   cd backend
   python manage.py runserver
   ```

2. **Access website:**
   - Homepage: `http://localhost:8000/`
   - Product: `http://localhost:8000/product.html?slug=combo-bundle`
   - Checkout: `http://localhost:8000/checkout.html?slug=combo-bundle`
   - API: `http://localhost:8000/api/products/`
   - Admin: `http://localhost:8000/admin/`

## 📦 Collecting Static Files (Production)

For production, collect static files:

```bash
python manage.py collectstatic
```

This collects all static files into `backend/staticfiles/` for deployment.

## ✅ Benefits

1. **Standard Django Structure** - Follows Django best practices
2. **Easy Management** - All files organized in one place
3. **Static File Serving** - Django handles static files automatically
4. **Template System** - Can use Django template features
5. **Production Ready** - Easy to deploy with proper static file handling

---

**All files are now properly organized under the backend folder!** 🎉


