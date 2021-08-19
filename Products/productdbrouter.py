from .models import *


class ProductDBRouter:
    def db_for_read(self, model, **hints):
        if (model == Product):
            # your model name as in settings.py/DATABASES
            return 'user_db'
        return None

    def db_for_write(self, model, **hints):
        if (model == Product):
            # your model name as in settings.py/DATABASES
            return 'user_db'
        return None