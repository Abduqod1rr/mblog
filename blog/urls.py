from django.urls import path
from .views import Homeview
from users.views import RegisterUseview ,LoginUserView 

urlpatterns = [
    path('/',Homeview.as_view(),name='home'),
    path('register',RegisterUseview.as_view(),name='register'),
    path('login',LoginUserView.as_view(),name='login')
]


