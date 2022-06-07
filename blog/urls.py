from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.lista_post, name='posts'),
    path("<int:post_id>", views.detalle_post, name='post_detail'),
    
]
 






