from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewList.as_view()),
    path('<int:pk>/', views.ReviewsById.as_view()),
    #path('product/<int:pk>/', views.reviews_by_product)
]