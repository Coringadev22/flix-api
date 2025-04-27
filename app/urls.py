
from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetriveUpdateView
from actors.views import ActorCreateListView, ActorRetriveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetriveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetriveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(), name="genre-create-list"),   
    path('genres/<int:pk>', GenreRetriveUpdateView.as_view(), name="genre-detail-view"),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetriveUpdateDestroyView.as_view(), name='actor-detail-view'),

    path('movie/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movie/<int:pk>/', MovieRetriveUpdateDestroyView.as_view(), name='movie-detail-view'),

    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetriveUpdateDestroyView.as_view(), name='review-detail-view'),
]

