from django.urls import path
from streaming.views import user_reviews
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>', views.movie, name='movie'),
    path('user/<int:user_id>/', user_reviews, name='user_reviews'),
    path('subscriptionplan/<int:subscription_id>/', views.subscription_plan_movies, name='subscription_plan_movies'),


]

