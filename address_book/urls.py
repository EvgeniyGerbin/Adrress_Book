from address_book.views import *
from django.urls import path

urlpatterns = [
    path('', PersonPageView.as_view(), name='base'),
    path('add/', PersonCreateView.as_view(), name='create_person'),
    path('update_person/<int:pk>', PersonUpdateView.as_view(), name='update_person'),
    path('delete_person/<int:pk>', PersonDeleteView.as_view(), name='delete_person'),
    path('search/', Search.as_view(), name='search'),

]