import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = os.environ.get('TELEGRAM_TOKEN')
updater = Updater(token)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
        text='Hello!')

def greeting(update, context):
    name = ' '.join(context.args)
    update.message.reply_text('Hello, {}!'.format(name))

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
        text=update.message.text)

def main():
    start_handler = CommandHandler('start', start)
    greeting_handler = CommandHandler('greet', greeting)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo) 
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(greeting_handler)
    updater.dispatcher.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

'''
Done! Congratulations on your new bot. You will find it at t.me/heeYop5ebot. You can now add a description, 
about section and profile picture for your bot, see /help for a list of commands. By the way, 
when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. 
Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
5044895054:AAEiNpf8Zvf9sQig_D-MkXjZYjy9AuOakGs
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
'''