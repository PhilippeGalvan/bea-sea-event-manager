from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.ReportListView.as_view()),
]