
from django.apps import AppConfig, apps
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.unregister(ContentType)
