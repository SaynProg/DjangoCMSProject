from . import views
from django.urls import path

urlpatterns = [
	path('', views.ContactView, name='contact_index'),
]