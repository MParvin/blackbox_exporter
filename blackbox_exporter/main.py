from email import message
from fastapi import FastAPI
from blackbox_exporter.notifications.telegram import send_message_to_telegram

app = FastAPI()


@app.get("/")
def index():
    return {"message": "App is running"}
 
@app.get("/sms")
def sms():
    return {"message": "Send SMS"}

@app.get("/telegram")
async def telegram():
    message = "Send Telegram"
    await send_message_to_telegram(message)
    return {"message": "Send Telegram"}
