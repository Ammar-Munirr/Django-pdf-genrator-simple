from django.urls import path
from . import views



urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('pdf_gen/',views.pdf_gen,name='pdf-gen')
]