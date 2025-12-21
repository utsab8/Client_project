# Server Restart Instructions

## The Problem
The server is showing old URL patterns because it's using cached Python bytecode.

## Solution: Complete Server Restart

### Step 1: Stop ALL Python Processes
1. Open Task Manager (Ctrl+Shift+Esc)
2. Find all `python.exe` processes
3. End all of them
4. OR use this command:
   ```powershell
   Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force
   ```

### Step 2: Clear Python Cache
```powershell
cd backend
Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force api\__pycache__ -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force skillcart_backend\__pycache__ -ErrorAction SilentlyContinue
```

### Step 3: Start Server Fresh
```bash
cd backend
python manage.py runserver
```

### Step 4: Test URLs
- Homepage: http://127.0.0.1:8000/
- Alternative: http://127.0.0.1:8000/home/
- Product: http://127.0.0.1:8000/product.html?slug=combo-bundle
- API: http://127.0.0.1:8000/api/products/

## Verification
The URL patterns should show:
1. (empty) - Homepage
2. home/ - Alternative homepage
3. product.html - Product page
4. checkout.html - Checkout page
5. admin/ - Admin panel
6. api/ - API endpoints

If you still see only `admin/` and `api/`, the server hasn't restarted properly.


