from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import include
from django.urls import path
urlpatterns += [
     path('rrs/', include('rrs.urls')),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/rrs/', permanent=True)),
]

