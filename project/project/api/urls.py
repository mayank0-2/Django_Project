from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . views import PostViewSet


router = SimpleRouter()

router.register('posts', PostViewSet)

urlpatterns = router.urls
