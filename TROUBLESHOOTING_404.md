# Troubleshooting 404 Error

If you're still getting a 404 error, try these steps:

## Step 1: Stop All Python Processes
```powershell
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Step 2: Clear Python Cache
```powershell
cd backend
Remove-Item -Recurse -Force __pycache__, api\__pycache__, skillcart_backend\__pycache__ -ErrorAction SilentlyContinue
```

## Step 3: Verify Files Exist
```powershell
# Check templates
Test-Path templates\index.html
Test-Path templates\product.html
Test-Path templates\checkout.html

# Check views
Test-Path api\views_frontend.py
```

## Step 4: Test URL Resolution
```bash
cd backend
python manage.py shell
```
Then in the shell:
```python
from django.urls import resolve
resolve('/')
```

## Step 5: Restart Server
```bash
cd backend
python manage.py runserver
```

## Alternative: Use Explicit Home Route

If the empty path still doesn't work, we can use an explicit route like `home/` or `index/`.


