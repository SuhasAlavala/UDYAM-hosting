from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import Dashboard, Team_delete, Update_User

urlpatterns = [
    path('dashboard', Dashboard, name='dashboard'),
    path('team-delete/<int:id>', Team_delete, name='team-delete'),
    path('update-user', Update_User, name='update-user')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)