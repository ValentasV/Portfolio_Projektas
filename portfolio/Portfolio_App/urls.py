from django.urls import path
from .views import ProfilisIrProjektasView, ProjektasListView

urlpatterns = [

    path('profiliai/', ProfilisIrProjektasView.as_view(), name='profiliai'),
    # path('profiliai/', ProfilisIrProjektai, name='profiliai'), # Alternatyvus kelias pagal funkciją  -  ProfilisIrProjektai
    path('', ProjektasListView.as_view(), name='projekto-info'),



]
