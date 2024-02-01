from django.urls import path

# local import
from .views import *


urlpatterns = [
    path('register/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('send-otp-email/', ForgotPasswordView.as_view(), name='send-otp-to-email'),
    path('enter-otp/', ValidateOTPView.as_view(), name='enter-otp'),
    path('new-password/', SetNewPasswordView.as_view(), name='set-new-password'),
] 


