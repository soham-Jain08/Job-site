"""
URL configuration for JobSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls.static import static
from . import settings
from accounts.views import *
from jobs.views import *
from bookmarks.views import *

urlpatterns = [
        path('admin/', admin.site.urls),
        path('register/', signup, name='signup'),
        path('login/', login_view, name='login'),
        path('logout/', logout_view, name='logout'),
        path('', job_list, name='home'),
        path('my_bookmarks/', user_bookmarks, name='user_bookmarks'),
        path('job_detail/<slug:slug>/', job_detail, name='job_detail'),
        path('bookmark/<int:job_id>/', toggle_bookmark, name='toggle_bookmark'),
        path('update_profile/', build_profile, name='update_profile'),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
