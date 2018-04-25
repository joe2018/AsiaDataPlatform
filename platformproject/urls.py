"""AsiaDataPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path
from platformproject import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index,name = 'index'),
    path('m_money/', views.m_money, name='m_money'),
    path('rofth_data/', views.rofth_data, name='rofth_data'),
    path('rofid_data/', views.rofid_data, name='rofid_data'),
    path('e3kid_data/', views.e3kid_data, name='e3kid_data'),
    path('game_data/', views.game_data, name='game_data'),
    path('favicon.ico',RedirectView.as_view(url=r'static/favicon.ico')),
    path('login/', views.login,name = 'login'),
    path('del_user/', views.del_user, name='del_user'),
]