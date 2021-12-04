"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from SearchEngine import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adv_search/', views.adv_search),
    path('index/', views.index),
    path('search/<str:query>/', views.adv_search, name='search'),
    path("getdoc/<str:nct_id>/", views.getdoc, name="getdoc"),
]
