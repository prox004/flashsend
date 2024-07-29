from django.contrib import admin
from django.urls import path
from share import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.submit_text, name='submit_text'),  # Make the submit view the home page
    path('submit/', views.submit_text, name='submit_text'),
    path('retrieve/', views.retrieve_text, name='retrieve_text'),
]
