from django.urls import path
from views import BookViewSet, StudentViewSet, StudentBookViewSet


urlpatterns = [
    path('book/', BookViewSet.as_view({'get':'list'}), name='book'),
]