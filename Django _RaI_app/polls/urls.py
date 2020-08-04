from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
     path('home/', views.home, name='home'),
    path('daily/', views.daily, name='daily'),
    path('weekly/', views.weekly, name='weekly'),
    path('monthly/', views.monthly, name='monthly'),
    path('chart/', views.chart, name='chart'),
    path('base/', views.chart, name='base'),
    path('post/',views.main_page1,name='main_page1'),
]