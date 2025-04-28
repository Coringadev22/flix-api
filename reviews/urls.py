from . import views
from django.urls import path


urlpatterns = [

    path('reviews/',
          views.ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/',
          views.ReviewRetriveUpdateDestroyView.as_view(), name='review-detail-view'),

]