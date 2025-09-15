from django.urls import path
from .views import Homeview ,AddCommentView
from users.views import RegisterUseview ,LoginUserView ,LogoutUserVIew

urlpatterns = [
    path('/',Homeview.as_view(),name='home'),
    path('register',RegisterUseview.as_view(),name='register'),
    path('login',LoginUserView.as_view(),name='login'),
    path('logout',LogoutUserVIew.as_view(),name='logout'),
    path('post/<int:post_pk>/comment',AddCommentView.as_view(),name='add_comment')

]


