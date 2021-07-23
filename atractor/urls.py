from django.contrib import admin
from django.urls import path, include

from blog.views import frontpage, post_detail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('accounts/login/', auth_views.LoginView.as_view()),
]
