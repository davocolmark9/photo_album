import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photo_album_project.settings')

application = get_wsgi_application()

# Run migrations on startup (only in production)
if os.environ.get('RENDER') == 'true':
    from django.core.management import call_command
    call_command('migrate', '--noinput')