from .models import *


class UserDBRouter:
    route_app_labels = {'User', 'Post'}
    def db_for_read(self, model, **hints):
        if (model == User):
           
            return 'user_db'
        return None

    def db_for_write(self, model, **hints):
        if (model == User):
           
            return 'user_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

class PostDBRouter:
    route_app_labels = {'User', 'Post'}
    def db_for_read(self, model, **hints):
        if (model == Post):
         
            return 'user_db'
        return None

    def db_for_write(self, model, **hints):
        if (model == Post):
 
            return 'user_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None