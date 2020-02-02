from django.urls import include, path
from django.contrib import admin


from polls1 import views


urlpatterns = [
    path('', include('polls1.urls')),
    path('admin/', admin.site.urls),
]