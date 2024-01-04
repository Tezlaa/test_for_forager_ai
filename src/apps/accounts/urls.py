from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from apps.accounts.views import SignUpUser


urlpatterns = [
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
