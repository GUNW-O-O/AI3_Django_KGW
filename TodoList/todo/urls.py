from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo, name='todo'),
    # path('create', views.create, name='create'),
    path('delete/<int:todo_no>', views.delete, name='delete'),
    path('ing', views.ing, name='ing'),
    path('done', views.done, name='done'),
    path('wait', views.wait, name='wait'),
    path('read/<int:todo_no>',views.read, name='read'),
    path('update/<int:todo_no>',views.update, name='update'),
]