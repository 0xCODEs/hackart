from django.conf.urls import *

#Django Rest Framework
from rest_framework import routers
from api import views

#REST API routes
router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'likes', views.LikeViewSet)
#router.register(r'userprofiles', views.UserprofileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    #Django Rest Auth
    url(r'^auth/', include('rest_framework.urls')),
]