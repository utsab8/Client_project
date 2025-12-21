# Skillcart - Digital Product E-Commerce Platform

A complete e-commerce platform for selling digital products (Reels Bundles) built with Django REST Framework backend and dynamic frontend.

## 🚀 Features

- **Django REST Framework API** - Complete backend with MySQL database
- **Dynamic Frontend** - JavaScript API client for dynamic content loading
- **Product Management** - Full CRUD operations for products, categories, and tags
- **Order Management** - Complete order processing system
- **Admin Panel** - Django admin for easy content management
- **Responsive Design** - Mobile-friendly UI
- **SEO Optimized** - Clean URLs and meta tags

## 📁 Project Structure

```
skillcart/
├── backend/                    # Django REST Framework Backend
│   ├── api/                    # Main API application
│   │   ├── models.py          # Database models
│   │   ├── serializers.py     # API serializers
│   │   ├── views.py           # API viewsets
│   │   ├── urls.py            # API URL routing
│   │   └── management/        # Management commands
│   ├── skillcart_backend/     # Django project settings
│   ├── manage.py
│   └── requirements.txt
├── html/                       # Frontend HTML files
│   ├── index.html             # Homepage (static)
│   ├── index-dynamic.html     # Homepage (dynamic example)
│   ├── products/              # Product detail pages
│   └── checkout/             # Checkout pages
├── css/                        # Stylesheets
│   └── style.css
├── js/                         # JavaScript files
│   ├── script.js              # Original frontend scripts
│   └── api.js                 # API client for dynamic content
├── SETUP_GUIDE.md             # Detailed setup instructions
└── README.md                  # This file
```

## 🛠️ Quick Start

### Prerequisites

- Python 3.8+
- MySQL 5.7+
- pip (Python package manager)

### Backend Setup

1. **Navigate to backend directory:**
```bash
cd backend
```

2. **Create virtual environment:**
```bash
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create MySQL database:**
```sql
CREATE DATABASE skillcart_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

5. **Configure database settings:**
   - Edit `backend/skillcart_backend/settings.py` or set environment variables
   - Update `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`

6. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create admin user:**
```bash
python manage.py createsuperuser
```

8. **Populate initial data:**
```bash
python manage.py populate_initial_data
```

9. **Start development server:**
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

### Frontend Setup

1. **Update API URL (if needed):**
   - Edit `js/api.js` and update `API_BASE_URL` if your backend is on a different port

2. **Test the dynamic homepage:**
   - Open `html/index-dynamic.html` in your browser
   - Products should load automatically from the API

3. **Integrate with existing pages:**
   - Add `<script src="../js/api.js"></script>` to your HTML files
   - The API client will automatically handle dynamic loading

## 📚 API Endpoints

### Products
- `GET /api/products/` - List all products
- `GET /api/products/{id}/` - Get product details
- `GET /api/products/featured/` - Get featured products
- `GET /api/products/by_price/?min_price=100&max_price=500` - Filter by price
- `GET /api/products/by_category/?category=slug` - Filter by category

### Categories
- `GET /api/categories/` - List all categories
- `GET /api/categories/{slug}/` - Get category details
- `GET /api/categories/{slug}/products/` - Get products in category

### Orders
- `POST /api/orders/` - Create new order
- `GET /api/orders/{id}/` - Get order details
- `PATCH /api/orders/{id}/update_status/` - Update order status
- `GET /api/orders/by_email/?email=user@example.com` - Get orders by email

### Settings
- `GET /api/settings/` - Get site settings

## 🗄️ Database Models

- **Product** - Products with pricing, images, descriptions, features
- **Category** - Product categories
- **Tag** - Product tags for filtering
- **Order** - Customer orders with payment tracking
- **SiteSettings** - Site-wide configuration

## 🎨 Frontend Integration

The `api.js` file provides a complete API client with helper functions:

```javascript
// Get all products
const products = await api.getProducts();

// Get product by slug
const product = await api.getProductBySlug('combo-bundle');

// Create order
const order = await api.createOrder({
    email: 'customer@example.com',
    phone: '1234567890',
    product: 1,
    quantity: 1
});
```

## 📖 Documentation

- **Setup Guide:** See `SETUP_GUIDE.md` for detailed setup instructions
- **Backend README:** See `backend/README.md` for API documentation
- **Django Docs:** https://docs.djangoproject.com/
- **DRF Docs:** https://www.django-rest-framework.org/

## 🔧 Configuration

### Environment Variables

Set these environment variables or update `settings.py`:

- `DB_NAME` - MySQL database name
- `DB_USER` - MySQL username
- `DB_PASSWORD` - MySQL password
- `DB_HOST` - MySQL host (default: localhost)
- `DB_PORT` - MySQL port (default: 3306)

### API Base URL

Update `API_BASE_URL` in `js/api.js` if your backend runs on a different URL.

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Set a strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Restrict CORS origins
- [ ] Use production database credentials
- [ ] Set up SSL/HTTPS
- [ ] Configure static file serving
- [ ] Set up database backups
- [ ] Use environment variables for secrets

## 🐛 Troubleshooting

### MySQL Connection Issues
- Ensure MySQL server is running
- Verify database credentials
- Check MySQL port accessibility

### CORS Errors
- Verify `CORS_ALLOW_ALL_ORIGINS = True` in settings (development)
- Check API URL matches Django server URL

### Products Not Loading
- Check browser console for errors
- Verify API is accessible
- Ensure `populate_initial_data` was run
- Check products exist in admin panel

## 📝 License

This project is for educational purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues or questions:
- Check the setup guide: `SETUP_GUIDE.md`
- Review backend documentation: `backend/README.md`
- Check Django and DRF documentation

---

**Built with ❤️ using Django REST Framework**


