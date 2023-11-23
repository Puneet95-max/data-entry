from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import companyviewset


router= routers.DefaultRouter()
router.register(r'companies',companyviewset)

urlpatterns = [
   path('',include(router.urls))

]