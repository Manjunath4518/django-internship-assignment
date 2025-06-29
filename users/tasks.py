from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(user_id):
    from .models import User
    try:
        user = User.objects.get(id=user_id)
        subject = 'Welcome to Our Platform'
        message = f'Hi {user.username},\n\nThank you for registering with us!'
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]
        send_mail(subject, message, email_from, recipient_list)
        return f"Welcome email sent to {user.email}"
    except User.DoesNotExist:
        return "User not found"