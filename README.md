# Production Ready Django Photo Album Management System

## Features

- Django CBVs
- RBAC Authentication
- Cloudinary Storage
- PostgreSQL Ready
- Elegant Bootstrap UI
- Render Deployment Ready

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```