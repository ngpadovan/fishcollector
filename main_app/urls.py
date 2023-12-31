from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('fishes/', views.fishes_index, name='index'),
  path('fishes/<int:fish_id>/', views.fishes_detail, name='detail'),
  path('fishes/create/', views.FishCreate.as_view(), name='fishes_create'),
  path('fishes/<int:pk>/update', views.FishUpdate.as_view(), name="fishes_update"),
  path('fishes/<int:pk>/delete', views.FishDelete.as_view(), name="fishes_delete"),
  path('fishes/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]