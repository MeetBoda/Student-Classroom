"""student_classroom URL Configuration

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
from django.urls import path,include
from student_classroom import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('classes.urls')),
    path('', views.loginpage),
    path('login', views.login),
    path('signup', views.signup),
    path('JoinClass', views.addclass),
    path('joinclass', views.joinclass),
    path('Stream', views.StreamPage),
    path('People', views.PeoplePage),
    path('createClass', views.createClass),
    path('generateClassroom', views.generateClassroom),
    path('Doubt', views.DoubtPage),
    path('askdoubt', views.askdoubt),
    path('answerdoubt', views.answerdoubt),
    path('viewanswers', views.viewanswers),
    path('uploadmaterial', views.uploadmaterial),
    path('storematerial', views.storematerial),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)