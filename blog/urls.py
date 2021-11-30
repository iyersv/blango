# other imports
from blog.views import index
from django.urls import path

urlpatterns = [
    path("", index)
]