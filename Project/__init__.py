from flask import Flask, request, abort
import json
import requests
from Project.config import * #folder Project file config
app = Flask(__name__)

@app.route('/')
def index():
  return "Hello World!"

# ส่วน  Webhook
@app.route('/webhook', methods = ['POST','GET'])
def webhook():
    if request.method == 'POST':
      payload = request.json
      Reply_token = payload['events'][0]['replyToken']
      message = payload['events'][0]['message']['text']
      print(Reply_token)
      print(message)
      if 'สวัสดี' in message :
          Reply_messasge = 'สวัสดีค่ะ'
      ReplyMessage(Reply_token,Reply_messasge, channel_access_token ) # Channel access token
      return request.json, 200

    elif request.method == 'GET':
        return 'this is method get !!!' , 200
    else:
        abort(400)


def ReplyMessage(Reply_token, TextMassage, Line_Access_Token ):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'

  Authorization = 'Bearer {}'.format(Line_Access_Token) # channel_access_token
  print(Authorization)

  headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }
  data = {
        "replyToken":Reply_token,
        "messages":[{
          "type":"text",
          "text":TextMassage
        }]
  }

  data = json.dumps(data)
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
  print(r.text)
  return 200

# if __name__ == '__main__':
#   app.run(debug=True)
