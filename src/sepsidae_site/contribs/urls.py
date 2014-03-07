from rest_framework import routers

from .views import ContributorViewSet, InstitutionViewSet

router = routers.DefaultRouter()

router.register('contributor', ContributorViewSet)
router.register('institution', InstitutionViewSet)

urlpatterns = router.urls
