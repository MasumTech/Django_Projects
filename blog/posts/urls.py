from django.urls import path
from .views import (
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
)

urlpatterns = [

    path('', post_list, name='list'),
    path('create/',  post_create),
    path('<int:qid>/',  post_detail, name='detail'),
    path('<int:qid>/edit/',  post_update, name='update'),
    path('<int:qid>/delete/',  post_delete),

]
