from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import BookListApiView, BookCreateApiView,BookUpdateApiView,BookDeleteApiView,BookDetailApiView, BookUpdateDeleteApiView, \
    BookListCreateApiView, BookViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListApiView.as_view()),
    # path('books/<int:pk>/',BookDetailApiView.as_view()),
    # path('books/<int:pk>/update/',BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/',BookDeleteApiView.as_view()),
    # path('books/create/', BookCreateApiView.as_view()),
    # path('book/updatedelete/<int:pk>/', BookUpdateDeleteApiView.as_view()),
    # path('book/detailcreate/',BookListCreateApiView.as_view()),
    
    
]

urlpatterns = urlpatterns + router.urls