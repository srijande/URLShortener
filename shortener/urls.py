from django.urls import path
from . import views
app_name = "url"
urlpatterns = [
    path("", views.HomeView.as_view(), name='home-view'),
    path("short/create_post", views.create_post),
    path('<str:shortened_link>/', views.redirector, name="Redirector"),
]