from django.urls import path
from .models import Ebook, Review
from .views import EbookListCreateAPIView, EbookDetailsAPIView, ReviewCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    path('ebooks/', EbookListCreateAPIView.as_view(), name='ebooks-list'),
    path('ebooks/<int:pk>/', EbookDetailsAPIView.as_view(), name='ebooks-details'),
    path('ebooks/<int:ebook_pk>/review/', ReviewCreateAPIView.as_view(), name='ebooks-review'),
    path('review/<int:pk>', ReviewDetailAPIView.as_view(), name='review-detail'),
]
