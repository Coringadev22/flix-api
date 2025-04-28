from . import views
from django.urls import path


urlpatterns = [
    
    path('movie/',
      views.MovieCreateListView.as_view(), name='movie-create-list'),
    path('movie/<int:pk>/',
      views.MovieRetriveUpdateDestroyView.as_view(), name='movie-detail-view'),

]