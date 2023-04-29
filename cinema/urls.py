from django.urls import path
from . import views

urlpatterns = [
    path('',views.startpage, name="startpage"),
    path('<film_name>', )
    path('reservation',views.reservation, name="reservation")
]

