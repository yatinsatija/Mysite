from django.urls import path

from . import views


urlpatterns = [
    path('store/', views.storeapi.as_view()),
    path('eventpool/', views.eventapi.as_view()),
    path('data/',views.main_page,name="main_page"),
]