import random
import string
from django.core.mail import EmailMessage 
from django.utils.html import format_html 
import random
import string
from django.conf import settings 
from rest_framework_simplejwt.tokens import RefreshToken



def get_tokens_for_user(user):
        '''get jwt token'''
        refresh = RefreshToken.for_user(user)

        return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
        }


def generate_otp(otp_size=6): 
        ''' generates 6 digits otp for password reset '''
        digits = string.digits 
        otp = ''.join([random.choice(digits) for _ in range(otp_size)])
        return otp


class EmailUser: 
        @staticmethod
        def send_email(data): 
                email = EmailMessage(
                        subject=data.get('subject'),
                        body=data.get('body'),
                        from_email =  settings.EMAIL_HOST_USER,  
                        to=[data.get('recipient_email')]
                )
                print(data)
                print('Sending email...')
                email.content_subtype = 'html'
                email.send()
                

def format_email(user, **kwargs): 
        if 'send_otp' in kwargs: 
                otp = kwargs.get('otp', None)
                email_body = format_html(
                ''' 
                Howdy {}! <br> <br>
                You requested to reset your password in Task Manager App. We forget, it happens, after all - we all are humans!<br> <br>
                Here is your OTP <strong>{}</strong> to reset your password. Never share this OTP with anyone. <br> <br>
                Remember, this OTP is only valid for 5 minutes! <br> <br>

                <br><br><br><br>

                Thank you, <br>
                Task Manager Team. <br> 
                                        
                ''', user.username, otp)
                # print(user.username, user.email)
                data = {
                    'subject' : 'Reset Your Password in Task Manager!',
                    'body' : email_body, 
                    'recipient_email' : user.email, 
                }
                return data