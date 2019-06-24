"""config URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import defaults as default_views

# for displaying the default boilerplate view
from django.views.generic import TemplateView


# remove this when you have views
from django.views import debug

urlpatterns = [

    # this will show the default django view
    path('', debug.default_urlconf, name='django_home'),
    path('home/', TemplateView.as_view(template_name='home.html')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += (
        path('400/',
            default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}),
        path('403/',
            default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}),
        path('404/',
            default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}),
        path('500/',
            default_views.server_error),
    )

# Basic admin customization
admin.site.site_header = f"{settings.MY_SITE_NAME} Administration "
admin.site.site_title = f"{settings.MY_SITE_NAME} Administration"
