
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='homesite'),
    path('donorreg/', include('dreg.urls'), name='dregsite'),
    path('search/', include('search.urls'), name='searchsite'),
    path('about/', include('dabout.urls'), name='aboutsite'),
    path('contact/', include('contact.urls'), name='contactsite')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header='NCI Blood Bank Admin'
admin.site.site_title='NCI Blood Bank Admin'
admin.site.index_title=' '

