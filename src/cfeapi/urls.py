"""cfeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/updates/', include('updates.api.urls')),  # api/updates/1/ --> detail
    url(r'^api/auth/', include(('accounts.api.urls', 'accounts'), namespace='api-auth')),  # api/updates/1/ --> detail
    url(r'^api/status/', include(('status.api.urls', 'status'), namespace="api-status")),
    url(r'^api/user/', include(('accounts.api.user.urls', 'accounts'), namespace='api-user'))
]
