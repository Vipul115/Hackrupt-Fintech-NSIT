"""hackrupt URL Configuration

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

from django.contrib import admin
from django.urls import path
from Customer import views
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name=os.path.dirname(os.path.dirname( __file__ ))+'/Customer/Template/index.html')),
    #path('home/', views.Index.as_view()),
    path('customers/all/', views.CustomerList.as_view()),
    path('login/', views.CheckLogin.as_view()),
    path('user_panel/', views.UserPanel.as_view() , name='user_panel'),
    path('get_user_json/', views.GetUserJson.as_view()),
]

urlpatterns += staticfiles_urlpatterns()

