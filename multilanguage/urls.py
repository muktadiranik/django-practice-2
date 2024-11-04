from django.urls import path
from .views import bilingual_form_view

urlpatterns = [
    path("", bilingual_form_view, name='bilingual_form'),
]
