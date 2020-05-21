from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [

    path('snippets/', views.snipped_list),
    path('snippets/<int:pk>/', views.snipped_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)