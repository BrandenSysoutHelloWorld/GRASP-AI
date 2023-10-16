# DEFINE IMPORTS
from django.urls import path
from . import views

# DEFINE APP NAME: 'dashboard'
app_name = 'dashboard'

# URL Paths Resolved within the list: 'urlpatterns'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]

'''
Made with ❤️
--------------------
BRANDEN VAN STADEN -
    All Rights Reserved | OCTOBER 2023
-------------------------------------
'''