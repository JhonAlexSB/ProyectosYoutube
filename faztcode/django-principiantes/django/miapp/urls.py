from django.urls import path
form . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about)
]
