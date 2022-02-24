# from functools import cache
# from itertools import count
from time import time
from flask import Flask, request, jsonify,abort
import json
import requests
# import mariadb
import redis
import io 
import os
import sys
import numpy as np
# from MySQLdb import converters, connect, FIELD_TYPE
import mysql.connector

from Project.config import *   # folder Project file config
from Project.flextimetable import *   # folder Project file flextimetable
from Project.flexexam import *   # folder Project file flexexamtable
from Project.grades import *  # folder Project file gradess

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ImageSendMessage, StickerSendMessage, AudioSendMessage, FlexSendMessage
)
from linebot.models.template import *
from linebot import (
    LineBotApi, WebhookHandler
)

# class DB:
#   connection = None
#   @staticmethod
#   def connect():
#     # Custom converter for tinyint to boolean
#     conv = converters.conversions
#     def bool_decoder(val):
#       if int(val) == 0:
#         return False
#       return True
#     conv[FIELD_TYPE.TINY]= bool_decoder
#     DB.connection = connect(
#       host="demo_db",
#       user="root", 
#       port=3306, 
#       passwd="demo",
#       db="demo", 
#       conv=conv)
      
# connect to database
# try:
#     conn = mariadb.connect(
#         user="root",
#         password="123456",
#         host="localhost",
#         port=3306,
#         database="data"
#     )
# except mariadb.Error as e:
#     print(e)
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)

# print(conn)
# mycursor = conn.cursor()

app = Flask(__name__)
# cache = redis.Redis(host='redis', port=6379)

line_bot_api = LineBotApi(channel_access_token)

# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)
       

@app.route('/')
def index():
  # count = get_hit_count()
  return "hello World!!"
  # return "Hello World! i have been seen {} time.\n".format(count)

#   Webhook
@app.route('/webhook', methods = ['POST', 'GET'])
def webhook():
    if request.method == 'POST' :
      payload = request.json
      # print(payload)
      if payload != None : 
        # print(request.json)
        payload = request.json
        # print(payload)
        message = payload['events'][0]['message']['text']
        print(message)

        json_line = request.get_json(force=False,cache=False)
        json_line = json.dumps(json_line) # convert python dict to json string
        decoded = json.loads(json_line)  # convert json string to python dict
        # print(decoded)
        no_event = len(decoded['events'])
        # print(range(no_event))
        for i in range(no_event):
            event = decoded['events'][i]
            event_handle(event)
        return '',200
      
      else :
        print("no request")
        abort(400)

    elif request.method == 'GET':
        return 'this is method get !!!' , 200
    else:
        abort(400)


def event_handle(event):
    print(event)
    try:
        # userId = "Ud2490a17b992d4efd47494d6518a4ee5s"
        userId = event['source']['userId'] # get line userid
        # sql = "SELECT * FROM studentaccount WHERE line_userID = %s "
        # val = (userId,)
        # mycursor.execute(sql,val)
        # myresult = mycursor.fetchall()
        # print(myresult)

#         sql = "SELECT  s.studentcode,s.studentname,s.studentsurname,s.prefixname,s.line_userID,t.acadyear,t.semester,t.coursecode,t.coursename,t.studytype,t.weekday,t.timefrom,t.timeto,t.sec,t.room FROM studentaccount s , timetable t WHERE s.studentID = t.studentID and s.line_userID = %s "
#         val = (userId,)
#         mycursor.execute(sql,val)
#         myresult = mycursor.fetchall()
#         print(myresult)

    except:
        print('error cannot get userId')
        return ''

    try:
        rtoken = event['replyToken'] # get reply token
    except:
        print('error cannot get rtoken')
        return ''
    if 'message' in event.keys():
        try:
            msgType = event["message"]["type"]
            msgId = event["message"]["id"]
        except:
            print('error cannot get msgID, and msgType')
            sk_id = np.random.randint(1,17)
            replyObj = StickerSendMessage(package_id=str(1),sticker_id=str(sk_id))
            line_bot_api.reply_message(rtoken, replyObj)
            return ''
    if msgType == "text":
        msg = str(event["message"]["text"])
        replyObj = handle_text(msg)
        line_bot_api.reply_message(rtoken, replyObj)
    return ''

from linebot.models import (TextSendMessage,FlexSendMessage)
def handle_text(inpmessage):
    
    if "สอบถามตารางเรียน / class schedule" in message:                  
                flex = flex_timetable()
                print(flex)
                flexdict = json.loads(flex)     # convert json string to python dict
                print(flexdict)
                replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flex)
                #  print(replyObj)


        # time exam test
        if "สอบถามตารางสอบ / exam schedule" in message:
                flex = flex_timeexam()
                print(flex)
                flexdict = json.loads(flex)     # convert json string to python dict
                print(flexdict)
                replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flexdict)
            #   print(replyObj)

            # grade table test
        if "สอบถามผลการศึกษา / grade result" in message:

                flex = flex_grades()
                print(flex)
                flexdict = json.loads(flex)     # convert json string to python dict
                print(flexdict)
                replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flexdict)
            #   print(replyObj)


        if "ระบบทะเบียนออนไลน์ / registration" in message :
            flex = flex_regismenu()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='การลงทะเบียนออนไลน์', contents=flexdict)
            # print(replyObj)

        if "เตรียมพร้อมก่อนการลงทะเบียน" in message :
            flex = flex_regisAnswer1()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict                print(flexdict)
            replyObj = FlexSendMessage(alt_text='เตรียมพร้อมก่อนการลงทะเบียน', contents=flexdict)
            # print(replyObj)

        if "ลืมรหัสผ่านเข้าระบบ" in message :
            flex = flex_regisAnswer2()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='ลืมรหัสผ่านเข้าระบบ', contents=flexdict)
            # print(replyObj)

        if "บัตรประจำตัวนิสิตหาย" in message :
            flex = flex_regisAnswer3()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='บัตรประจำตัวนิสิตหาย', contents=flexdict)
            # print(replyObj)

        if "เปลี่ยนแปลงข้อมูลส่วนตัว" in message :
            flex = flex_regisAnswer4()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='เปลี่ยนแปลงข้อมูลส่วนตัว', contents=flexdict)
            # print(replyObj)

        if "ไม่ได้ลงทะเบียนเรียน/ชำระเงิน" in message :
            flex = flex_regisAnswer5()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='ไม่ได้ลงทะเบียนเรียน/ชำระเงิน', contents=flexdict)
            # print(replyObj)

        if "ติดต่อ" in message :
            flex = flex_regisAnswer6()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='ติดต่อ', contents=flexdict)
            # print(replyObj) 


        if "การชำระค่าทำเนียมการศึกษา / tuition fee payment" in message : 
            flex = flex_paymentmenu()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='การชำระค่าทำเนียมการศึกษา', contents=flexdict)
            # print(replyObj)

        if "การชำระเงินและพิมพ์ใบแจ้งการชำระเงิน" in message :
            flex = flex_paymentAnswer1()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='การชำระเงินและพิมพ์ใบแจ้งการชำระเงิน', contents=flexdict)
            # print(replyObj) 

        if "ช่องทางการชำระเงิน" in message :
            flex = flex_paymentAnswer2()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='ช่องทางการชำระเงิน', contents=flexdict)
            # print(replyObj) 

        if "ตรวจสอบสถานะการชำระเงินและพิมพ์ใบเสร็จ" in message :
            flex = flex_paymentAnswer3()
            print(flex)
            flexdict = json.loads(flex)     # convert json string to python dict
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='ตรวจสอบสถานะการชำระเงินและพิมพ์ใบเสร็จ', contents=flexdict)
            # print(replyObj) 

        if "ติดต่อเพิ่มเติม / contactmore" in message :
            flex = contact()
            print(flex)
            flexdict = json.loads(flex)
            print(flexdict)
            replyObj = FlexSendMessage(alt_text='ติดต่อ', contents=flexdict)
            # print(replyObj)
#     if inpmessage == 'สอบถามตารางเรียน':
#       flex = flex_timetable()
#       flex = json.loads(flex)     # convert json string to python dict
#       # print(flex)
#       replyObj = FlexSendMessage(alt_text='ตารางเรียนของคุณ', contents=flex)
#    #   print(replyObj)
#     else:
#       replyObj = TextSendMessage(text=inpmessage)

#     if inpmessage == 'สอบถามตารางสอบ':
#       flex = examtable()
#       flex = json.loads(flex)     # convert json string to python dict
#     #   print(flex)
#       replyObj = FlexSendMessage(alt_text='ตารางสอบของคุณ', contents=flex)
#       print(replyObj)     

#     if inpmessage == 'สอบถามเกรด':
#       flex = grades()
#       flex = json.loads(flex)     # convert json string to python dict
#     #   print(flex)
#       replyObj = FlexSendMessage(alt_text='เกรดของคุณ', contents=flex)
#       print(replyObj)    

#     if 'สวัสดี' in inpmessage :
#         replyObj = TextSendMessage(text='สวัสดีค่ะ')
  
#     if 'hi' in inpmessage :
#         replyObj = TextSendMessage(text='hello')

    return replyObj

# def ReplyMessage(Reply_token, TextMassage, Line_Access_Token ):
#   LINE_API = 'https://api.line.me/v2/bot/message/reply'

#   Authorization = 'Bearer {}'.format(Line_Access_Token) # channel_access_token
#   print(Authorization)

#   headers = {
#         'Content-Type': 'application/json; charset=UTF-8',
#         'Authorization':Authorization
#     }
#   data = {
#         "replyToken":Reply_token,
#         "messages":[{
#           "type":"text",
#           "text":TextMassage
#         }]
#   }

#   data = json.dumps(data)
#   r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล
#   print(r.text)
  # return 200

# def Reply_Flex(user, flex_message, Line_Acees_Token):
#     LINE_API = "https://api.line.me/v2/bot/message/push"

#     Authorization = 'Bearer {}'.format(Line_Acees_Token)
    
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization':Authorization
#     }
#     data = {
#         "to":str(user),
#         "messages":[{
#             "type": "flex",
#             "altText": "This is a Flex Message",
#             "contents":flex_message
#         }]
#     }
#     data = json.dumps(data) ## dump dict >> Json Object
#     r = requests.post(LINE_API, headers=headers, data=data) 
#     return 200

    
    
    # LINE_API = 'https://api.line.me/v2/bot/message/reply'

    # Authorization = 'Bearer {}'.format(bot_access_key)

    # headers = {'Content-Type': 'application/json; charset=UTF-8',
    # 'Authorization': Authorization}

    # file_data['replyToken'] = reply_token
    # #### dumps file จาก dict ให้เป็น json
    # file_data = json.dumps(file_data)
    # r = requests.post(LINE_API, headers=headers, data=file_data) # ส่งข้อมูล

    # return 200

  # def Reply_Imagemap(user, imagemap_message, Line_Acees_Token):
  #   LINE_API = "https://api.line.me/v2/bot/message/push"
  #   Authorization = 'Bearer {}'.format(Line_Acees_Token)
  #   headers = {
  #       'Content-Type': 'application/json',
  #       'Authorization':Authorization
  #   }
  #   data = {
  #       "to":str(user),
  #       "messages":[{
  #           "type": "imagemap",
  #           "altText": "This is a 'Imagemap",
  #           "contents":flex_message
  #       }]
  #   }
  #   data = json.dumps(data) ## dump dict >> Json Object
  #   r = requests.post(LINE_API, headers=headers, data=data) 
  #   return 200

# if __name__ == '__main__':
#   app.run(debug=True)
