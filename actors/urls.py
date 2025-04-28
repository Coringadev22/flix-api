from . import views
from django.urls import path

urlpatterns = [
    
    path('actors/',
      views.ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/',
      views.ActorRetriveUpdateDestroyView.as_view(), name='actor-detail-view'),

]