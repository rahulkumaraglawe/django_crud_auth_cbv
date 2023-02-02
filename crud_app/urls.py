from django.urls import path
from .views import SaveView, ShowView


urlpatterns = [
    path('save/', SaveView.as_view(), name='save_url'),
    path('show/', ShowView.as_view(), name='show_url')
]