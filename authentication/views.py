from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models  import User
from django.contrib import messages 
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response 
from rest_framework import status

# local import
from .forms import SingUpForm, EmailForOTPForm, NewPasswordForm, OTPForm
from .utils import generate_otp, EmailUser, format_email, get_tokens_for_user
# Create your views here.

class SignUpView(CreateView):
    '''User sign up it takes username, first name, last name, password and confirm password'''
    form_class = SingUpForm
    template_name = 'authentication/signupForm.html'
    success_url = reverse_lazy('login')


    def dispatch(self, request, *args, **kwargs):
        '''if user already logged in'''
        if self.request.user.is_authenticated:
            messages.warning(self.request, 'You already logged in.')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'You successfully create account')
        response = super().form_valid(form)
        return response
    


class LoginView(FormView):
    '''Here user can log in by username and password'''
    form_class = AuthenticationForm
    template_name = 'authentication/loginForm.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        '''if user already logged in'''
        if self.request.user.is_authenticated:
            messages.warning(self.request, 'You already logged in.')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)
    

class LogoutView(View):
    '''User log out view'''
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('login'))
    





class ForgotPasswordView(FormView):
    '''Here validate user and send OTP by email if user forgot password'''
    template_name = 'authentication/send_otp_email.html'
    form_class = EmailForOTPForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(self.request, "Email doesn't match :(")
            return redirect('login')

        otp = generate_otp() # genarate OTP
        try:
            # formate and send this otp by email 
            email_body = format_email(user, otp=otp, send_otp=True) # use mehtod overloading
            EmailUser.send_email(email_body)
        except Exception as e:
            # print("***Exception ",e)
            messages.warning(self.request, "OTP didn't send, some info may be missing")
            return redirect('login')

        self.request.session['username'] = user.username
        self.request.session['otp'] = otp
        return redirect('enter-otp')


class ValidateOTPView(FormView):
    '''OTP validation'''
    template_name = 'authentication/otp_form.html'
    form_class = OTPForm

    def form_valid(self, form):
        # username = self.request.session.get('username')
        stored_otp = self.request.session.get('otp')
        otp = form.cleaned_data['otp']
        # print(stored_otp, otp)
        if otp == stored_otp:
            return redirect('set-new-password')
        messages.warning(self.request, 'Invalid OTP. Please try again.')
        return self.render_to_response(self.get_context_data(form=form))


class SetNewPasswordView(FormView):
    '''Set new password'''
    template_name = 'authentication/set_new_password.html'
    form_class = NewPasswordForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        username = self.request.session.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.warning(self.request, "User not found!")
            return redirect('login')

        new_password = form.cleaned_data['new_password']
        user.set_password(new_password)
        user.save()
        self.request.session.flush()
        messages.success(self.request, 'Successfully changed your password, now you can login')
        return super().form_valid(form)
    


####################### Get JWT token ##############################

'''Jwt token for testing postman'''

class LoginAPI(APIView): 
        ''' Authenticates an user with either username and password, and passes token '''
        def post(self, request):   
                username= request.data.get('username', None)
                password = request.data.get('password', None)

                user = authenticate(request, username=username,  password=password)
                if user is not None: 
                        token = get_tokens_for_user(user)
                        return Response({'status' : 'success', 'token' : token}, status=status.HTTP_200_OK)
                return Response({'status' : 'error', 'data' : {'non_field_errors' : ['Username or password is incorrect']}}, status=status.HTTP_404_NOT_FOUND)
   