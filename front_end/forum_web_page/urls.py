from django.urls import path

from front_end.forum_web_page.views import home

urlpatterns = [
    path('', home, name='home')
]
