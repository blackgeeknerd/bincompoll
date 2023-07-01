
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy

from django.urls import path
from bincomApp import views


# app_name = 'bincomApp'
urlpatterns = [
    path('', views.PollUnitResult, name='home' ),
    
    path('createpollunit/', views.New_PollUnit, name='new_poll_unit'),
    path('pollunitresults', views.PollUnitResult, name='poll-unit-results'),
]







# if settings.DEBUG:
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
