from django.urls import include, path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.post_list, name='home'),
    #path('addTodo/', addTodo),
    #path('deleteTodo/<int:todo_id',deleteTodo),
]
