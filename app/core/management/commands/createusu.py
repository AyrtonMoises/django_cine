from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):    

    def handle(self, *args, **options):
        #cria usuario administrador
        if not User.objects.filter(username="admin").exists():
            user = User.objects.create_superuser("admin", "admin@admin.com", "admin", first_name="Administrador")