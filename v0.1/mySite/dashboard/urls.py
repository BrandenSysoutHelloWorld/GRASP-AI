# DEFINE IMPORTS
from django.urls import path
from . import views

# DEFINE APP NAME: 'dashboard'
app_name = 'dashboard'

# URL Paths Resolved within the list: 'urlpatterns'
urlpatterns = [
    path('', views.landing_redirect, name='welcome'),
    path('dashboard/', views.dashboard, name='home'),
    path('grasp-pdf/', views.upload_pdf, name='grasp-pdf')
]

'''
Made with ❤️
--------------------
BRANDEN VAN STADEN -
    All Rights Reserved | OCTOBER 2023
-------------------------------------
'''