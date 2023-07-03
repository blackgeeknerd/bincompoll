
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
    path('lgscore/', views.ResultByLg, name='lga_score'),

]

