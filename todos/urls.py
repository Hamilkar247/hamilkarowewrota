from django.urls import include, path
from . import views

app_name = "todos"

urlpatterns = [
    path('', views.home, name='home'),
    #path('addTodo/', addTodo),
    #path('deleteTodo/<int:todo_id',deleteTodo),
]
