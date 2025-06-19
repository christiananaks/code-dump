from django.urls import path

from . import views

# we list all the urls we want to support and the view function
# that should be triggered when a request reaches that url
urlpatterns = [
    # creates a url conf
    # path('january', views.january),
    path('', views.index),  # /challenges/ nothing...
    path('<int:month>', views.monthly_challenge_by_number),  # only match this path if the dynamic segment value is a number
    # add a placeholder for dynamic url segment, convert path with str: in front of identifier like so <str:identifier>
    # name this urlpattern 'month-challenge' to help construct valid urls from other views
    path('<str:month>', views.monthly_challenge, name='month-challenge'),

]
