from django.urls import path
from . import views
from .create_site_view import CreateSiteView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login, name='login'),
    path('main/', CreateSiteView.as_view(), name='main')
]
