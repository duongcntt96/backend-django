from django.urls import include, path
from rest_framework import routers
from api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('restapi.urls')),
    path('admin/', admin.site.urls),
    path('xe/', include('xe.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
