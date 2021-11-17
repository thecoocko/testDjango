from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:hello_id>/results/',views.results,name="results"),
    path('<int:hello_id>/', views.detail, name='detail'),
]