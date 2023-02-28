from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home),
    path('home/', views.home),
    path('mygames/', views.mygames, name='mygames'),

    path('gta5/', views.gta,name='gta5'),
    path('ac/', views.ac, name='ac'),
    path('spiderman/', views.spiderman,name='spiderman'),
    path('uncharted/', views.uncharted, name='uncharted'),
    path('tombraider/', views.tombraider, name='tombraider'),
    path('dmc/', views.dmc, name='dmc'),
    path('cod/', views.cod, name='cod'),
    path('sam/', views.sam, name='sam'),
    path('division/', views.division, name='division'),
    path('nfs/', views.nfs, name='nfs'),

    path('payment_ac/', views.payment_ac, name='payment_ac'),
    path('payment_spiderman/', views.payment_spiderman, name='payment_spiderman'),
    path('payment_uncharted/', views.payment_uncharted, name='payment_uncharted'),
    path('payment_tombraider/', views.payment_tombraider, name='payment_tombraider'),
    path('payment_dmc/', views.payment_dmc, name='payment_dmc'),
    path('payment_cod/', views.payment_cod, name='payment_cod'),
    path('payment_sam/', views.payment_sam, name='payment_sam'),
    path('payment_division/', views.payment_division, name='payment_division'),
    path('payment_gta5/', views.payment_gta5, name='payment_gta5'),
    path('payment_nfs/', views.payment_nfs, name='payment_nfs'),
    
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
     
    path('paid/', views.paid, name='paid'),
     
]