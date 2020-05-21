from django.urls import path
from . import views

urlpatterns = [

    path('snippets/', views.snipped_list),
    path('snippets/<int:pk>/', views.snipped_detail),
]
