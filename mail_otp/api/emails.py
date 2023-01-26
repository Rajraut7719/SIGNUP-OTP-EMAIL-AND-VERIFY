from django.core.mail import send_mail
from .models import User
from django.conf import settings
import random
import os

def send_otp_email(email):
    subject = 'Your account verification email'
    otp = random.randint(100000,999999)
    message = f'Your otp is {otp}'
    email_from = os.getenv('EMAIL_HOST_USER')
    send_mail(subject,message,email_from,[email])
    user_obj = User.objects.get(email = email)
    user_obj.otp = otp
    user_obj.save()
