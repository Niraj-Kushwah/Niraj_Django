from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='Home'),
    path('Home', views.Home, name='Home'),
    path('Menu', views.Menu, name='Menu'),
    path('About', views.About, name='About'),
    path('Blog', views.Blog, name='Blog'),
    path('Customers', views.Customers, name='Customers'),
    path('Contact', views.Contact, name='Contact'),
    path('Export', views.Export, name='Export'),
    path('Search', views.Search, name='Search'),
    path('Signup', views.Signup, name='Signup'),
    path('Login', views.Login, name='Login'),
    path('Logout', views.Logout),
]