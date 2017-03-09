from django.conf.urls import *
#from rest_framework import routers
from api.views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

#REST API routes
router = routers.DefaultRouter()
router.register(r'challenges', ChallengeViewSet)
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'scoreboard', ScoreboardViewSet)
#router.register(r'users', views.UserViewSet)
#router.register(r'likes', views.LikeViewSet)
#router.register(r'userprofiles', views.UserprofileViewSet)

urlpatterns = [
    #Django Rest Auth
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
    url(r'^session/', csrf_exempt(Session.as_view())),
    #url(r'^challenges/', csrf_exempt(ChallengeView.as_view())),
]