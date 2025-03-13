from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('admin/',views.admin,name='admin'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    path('update<int:id>/',views.update,name='update'),
    path('delete<int:id>/',views.delete,name='delete'),
]