# Quick Fix for 404 Error

## The Issue
Django server might be caching old URL patterns or the server needs a fresh restart.

## Solution

### Option 1: Manual Server Restart
1. **Stop the server completely:**
   - Find the terminal/command prompt running the server
   - Press `Ctrl+C` to stop it
   - Wait a few seconds

2. **Clear Python cache:**
   ```powershell
   cd backend
   Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
   Remove-Item -Recurse -Force api\__pycache__ -ErrorAction SilentlyContinue
   Remove-Item -Recurse -Force skillcart_backend\__pycache__ -ErrorAction SilentlyContinue
   ```

3. **Start server fresh:**
   ```bash
   cd backend
   python manage.py runserver
   ```

### Option 2: Test Alternative Route
If `http://127.0.0.1:8000/` still doesn't work, try:
- `http://127.0.0.1:8000/home/` (alternative route I added)

### Option 3: Verify URL Configuration
Run this to see all URL patterns:
```bash
cd backend
python manage.py shell
```
Then:
```python
from django.urls import get_resolver
resolver = get_resolver()
for pattern in resolver.url_patterns:
    print(pattern.pattern)
```

## Current URL Configuration
- `/` → Homepage (index view)
- `/home/` → Homepage (alternative)
- `/product.html?slug=...` → Product page
- `/checkout.html?slug=...` → Checkout page
- `/admin/` → Django admin
- `/api/...` → API endpoints

## If Still Not Working
1. Check that `backend/api/views_frontend.py` exists
2. Check that `backend/templates/index.html` exists
3. Verify no syntax errors: `python manage.py check`
4. Try accessing: `http://127.0.0.1:8000/home/` instead


