from flask import Flask,request,abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import pya3rt
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

line_bot_api = LineBotApi("Ym1VfIw4a2BTRpvKdornxSm1uArvxiDDY9jaPJBXOHQ4g9TM29iGd0aVDS5qOJHzHiLt6xx8GavNwXpcAZAyMYxxt6aYf8d70q9vazN9i0MmZc0gDD2CWqml4lP79CJShEFBNlrUOT+spqFDPzukuAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("e9dd45e00f5417a4da3c4f38bfe7c7a1")

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
#    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  ai_message = talk_api(event.message.text)
  line_bot_api.reply_message(event.reply_token, TextSendMessage(text=ai_message))

def talk_api(word):
  apiKey = "DZZ9mYjEGCNKcoYVP7vzy1cguH1YVXOf"
  client = pya3rt.TalkClient(apiKey)
  reply_message = client.talk(word)
  return reply_message['results'][0]['reply']

if __name__ == '__main__':
  app.run()
