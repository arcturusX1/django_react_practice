from rest_framework.routers import DefaultRouter
from .views import UserMovieListViewSet

router = DefaultRouter()
router.register(r'user-movies', UserMovieListViewSet, basename="user-movies")

urlpatterns = router.urls 