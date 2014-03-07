from rest_framework import routers

from .views import SpeciesViewset, GenusViewset

router = routers.DefaultRouter()
router.register('species', SpeciesViewset)
router.register('genus', GenusViewset)

urlpatterns = router.urls
