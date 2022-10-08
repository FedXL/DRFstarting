"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from woman.views import WomenApiView, WomenApiList, WomenApiUpdate, WomenApiViewSet, WomenApiDestroy

router = routers.DefaultRouter()
router.register(r'women', WomenApiViewSet)

print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/womenlist", WomenApiList.as_view()),
    path("api/v1/womenlist/<int:pk>/", WomenApiList.as_view()),
    path("api/v2/womenlist", WomenApiList.as_view()),
    path("api/v2/womenupdate/<int:pk>/", WomenApiUpdate.as_view()),
    path("api/v2/womendestoy/<int:pk>/", WomenApiDestroy.as_view()),
    path("api/v3/",include(router.urls))
    # path("api/v3/womenlist", WomenApiViewSet.as_view({'get':'list'})),
    # path("api/v3/womenlist/<int:pk>/", WomenApiViewSet.as_view({'put':'update'}))
]
