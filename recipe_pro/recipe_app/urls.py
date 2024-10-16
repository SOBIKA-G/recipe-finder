from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
   path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('search/', views.search_recipes, name='search_recipes'),

]