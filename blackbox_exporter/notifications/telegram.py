import requests
from blackbox_exporter.config import return_conf
TELEGRAM_URL=return_conf('TELEGRAM_URL')
TELEGRAM_BOT_TOKEN=return_conf('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID=return_conf('TELEGRAM_CHAT_ID')

def send_message_to_telegram(message):
    url = '{}/bot{}/sendMessage'.format(TELEGRAM_URL,TELEGRAM_BOT_TOKEN)
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.get(url, params=payload)
    return True