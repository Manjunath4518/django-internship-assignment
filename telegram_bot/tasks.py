from celery import shared_task
from .handlers import setup_bot

@shared_task
def run_telegram_bot():
    setup_bot()