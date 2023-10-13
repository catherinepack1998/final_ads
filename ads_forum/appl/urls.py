from django.urls import path
from .views import *

urlpatterns = [
    path('', AdsList.as_view(), name='general'),
    path('ad/<int:pk>/', Ad.as_view()),
    path('ad/response/', add_response, name='add_response'),   
    path('cabinet/', AdResponseSearch.as_view(), name='cabinet'), 
    path('cabinet/add_ad/', add_ad, name='add_ad'),
    path('cabinet/response/<int:pk>/delete/', ResponseDeleteView.as_view(), name='delete'),
    path('cabinet/response/submit/', submit_response, name='submit'),
]