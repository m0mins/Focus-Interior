from django.contrib import admin
from django.urls import path,include
#from django.conf.urls import handler404
from focusInteriorApp import views

from django.conf import settings
from django.conf.urls.static import static
#handler404 = 'App_Home.views.custom_404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('focusInteriorApp.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)