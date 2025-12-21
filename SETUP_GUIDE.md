# Skillcart - Complete Setup Guide

This guide will help you set up the complete Skillcart website with Django REST Framework backend and dynamic frontend.

## Project Structure

```
skillcart/
├── backend/                 # Django REST Framework API
│   ├── api/                 # Main API app
│   ├── skillcart_backend/   # Django project settings
│   ├── manage.py
│   └── requirements.txt
├── html/                    # Frontend HTML files
├── css/                     # Stylesheets
├── js/                      # JavaScript files
│   ├── script.js           # Original frontend scripts
│   └── api.js              # API client for dynamic content
└── SETUP_GUIDE.md          # This file
```

## Step 1: Backend Setup

### 1.1 Install Python Dependencies

```bash
cd backend
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Note:** If `mysqlclient` installation fails, you can use `pymysql` instead:

```bash
pip install pymysql
```

Then add to `backend/skillcart_backend/__init__.py`:
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### 1.2 Setup MySQL Database

1. **Create MySQL Database:**
```sql
CREATE DATABASE skillcart_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. **Configure Database Settings:**

Edit `backend/skillcart_backend/settings.py` or set environment variables:

**Windows (PowerShell):**
```powershell
$env:DB_NAME="skillcart_db"
$env:DB_USER="root"
$env:DB_PASSWORD="your_password"
$env:DB_HOST="localhost"
$env:DB_PORT="3306"
```

**Linux/Mac:**
```bash
export DB_NAME=skillcart_db
export DB_USER=root
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_PORT=3306
```

### 1.3 Run Migrations

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 1.4 Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 1.5 Populate Initial Data

```bash
python manage.py populate_initial_data
```

This will create:
- Site settings
- Categories
- Tags
- All 12 products from your existing HTML files

### 1.6 Start Django Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## Step 2: Frontend Integration

### 2.1 Update HTML Files to Use API

You need to include the API client script in your HTML files. Add this before the closing `</body>` tag:

```html
<!-- API Client -->
<script src="../js/api.js"></script>
<!-- Original Script -->
<script src="../js/script.js"></script>
```

### 2.2 Update Homepage (index.html)

The homepage will automatically load products from the API. The `api.js` file includes functions that:
- Load products dynamically on page load
- Handle price filtering
- Render product cards

### 2.3 Update Product Pages

Product pages will automatically load product details based on the URL slug. For example:
- `products/combo-bundle.html` will load product with slug `combo-bundle`

### 2.4 Update Checkout Pages

Checkout forms will automatically submit to the API. Make sure the checkout page includes:

```html
<form id="checkoutForm">
    <input type="email" id="email" required>
    <input type="tel" id="phone" required>
    <button type="submit">Make Payment</button>
</form>
```

## Step 3: Testing

### 3.1 Test API Endpoints

Open your browser and test these URLs:

- `http://localhost:8000/api/products/` - List all products
- `http://localhost:8000/api/products/1/` - Get product by ID
- `http://localhost:8000/api/categories/` - List categories
- `http://localhost:8000/api/orders/` - List orders (after creating some)
- `http://localhost:8000/api/settings/` - Get site settings

### 3.2 Test Frontend

1. Open `html/index.html` in your browser
2. Products should load dynamically from the API
3. Click on a product to see details
4. Test the checkout form

### 3.3 Test Admin Panel

1. Go to `http://localhost:8000/admin/`
2. Login with your superuser credentials
3. You can manage products, orders, categories, and tags

## Step 4: Making Frontend Fully Dynamic

### Option 1: Update Existing HTML Files

You can update your existing HTML files to use the API. The `api.js` file handles most of the dynamic loading automatically.

### Option 2: Create Single Page Application (SPA)

For a fully dynamic experience, you could create a single-page application that:
- Loads all content from the API
- Uses client-side routing
- Updates content without page reloads

## API Usage Examples

### Get All Products
```javascript
const products = await api.getProducts();
```

### Get Product by Slug
```javascript
const product = await api.getProductBySlug('combo-bundle');
```

### Create Order
```javascript
const order = await api.createOrder({
    email: 'customer@example.com',
    phone: '1234567890',
    customer_name: 'John Doe',
    product: 1,
    quantity: 1,
    bump_offer_added: false,
    bump_offer_price: null
});
```

### Filter Products by Price
```javascript
const products = await api.getProductsByPrice(99, 199);
```

## Database Models

### Product
- name, slug, description
- price, original_price, discount_percentage
- image, image_url
- category, tags
- features, what_included, perfect_for
- is_active, is_featured

### Order
- email, phone, customer_name
- product, quantity
- unit_price, total_amount
- bump_offer_added, bump_offer_price
- status, payment_id
- download_link, download_sent

### Category
- name, slug, description

### Tag
- name, slug

### SiteSettings
- site_name, site_tagline
- whatsapp_number, instagram_url, youtube_url
- footer_links, meta_description

## Troubleshooting

### MySQL Connection Issues

1. **Check MySQL is running:**
```bash
# Windows
net start MySQL80

# Linux
sudo systemctl status mysql
```

2. **Verify database exists:**
```sql
SHOW DATABASES;
```

3. **Check user permissions:**
```sql
GRANT ALL PRIVILEGES ON skillcart_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

### CORS Issues

If you see CORS errors in the browser console, make sure:
- Django server is running
- `CORS_ALLOW_ALL_ORIGINS = True` is set in settings.py (for development)
- API URL in `api.js` matches your Django server URL

### Products Not Loading

1. Check browser console for errors
2. Verify API is accessible: `http://localhost:8000/api/products/`
3. Check that `populate_initial_data` command was run
4. Verify products exist in admin panel

### Images Not Showing

1. Product images are stored in `backend/media/products/`
2. Make sure `MEDIA_URL` and `MEDIA_ROOT` are configured correctly
3. In development, Django serves media files automatically
4. In production, configure your web server to serve media files

## Production Deployment

### Before Deploying:

1. **Security Settings:**
   - Set `DEBUG = False`
   - Set a strong `SECRET_KEY`
   - Configure `ALLOWED_HOSTS`
   - Restrict CORS origins

2. **Database:**
   - Use production database credentials
   - Set up database backups
   - Use connection pooling

3. **Static Files:**
   - Run `python manage.py collectstatic`
   - Configure web server to serve static files
   - Use CDN for media files

4. **Environment Variables:**
   - Use environment variables for sensitive data
   - Never commit secrets to version control

5. **SSL/HTTPS:**
   - Set up SSL certificates
   - Redirect HTTP to HTTPS
   - Use secure cookies

## Next Steps

1. **Payment Integration:**
   - Integrate payment gateway (Razorpay, Stripe, etc.)
   - Update order status after payment
   - Send download links via email

2. **Email Notifications:**
   - Send order confirmation emails
   - Send download links
   - Send payment receipts

3. **User Authentication:**
   - Add user registration/login
   - Track user orders
   - User dashboard

4. **Analytics:**
   - Track product views
   - Track conversions
   - Sales reports

5. **Search & Filters:**
   - Enhanced search functionality
   - Advanced filtering options
   - Sorting options

## Support

For issues or questions:
- Check Django documentation: https://docs.djangoproject.com/
- Check DRF documentation: https://www.django-rest-framework.org/
- Review the backend README: `backend/README.md`


