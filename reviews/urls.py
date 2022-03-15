from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list),
    path('<int:pk>/', views.reviews_by_id)
]