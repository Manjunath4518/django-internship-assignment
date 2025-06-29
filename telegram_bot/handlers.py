import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from django.conf import settings
from users.models import User
from .models import TelegramUser

def start(update, context):
    chat_id = update.message.chat.id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    
    # Try to find existing user
    user, created = User.objects.get_or_create(
        username=f"telegram_{username}",
        defaults={
            'first_name': first_name,
            'last_name': last_name,
            'telegram_username': username
        }
    )
    
    # Create or update TelegramUser
    telegram_user, created = TelegramUser.objects.update_or_create(
        user=user,
        defaults={
            'chat_id': chat_id,
            'username': username,
            'first_name': first_name,
            'last_name': last_name
        }
    )
    
    update.message.reply_text(
        f"Hello {first_name}! Your Telegram username {username} has been registered."
    )

def setup_bot():
    updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    
    # Start polling
    updater.start_polling()
    updater.idle()