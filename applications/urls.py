from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationListCreateView.as_view(), name='application-list'),
    path('<int:pk>/', views.ApplicationDetailView.as_view(), name='application-detail'),
]