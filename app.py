from flask import Flask,request
import json
import urllib.parse as parse
import urllib.request as req

app = Flask(__name__)

def baseRequest (command="getMe"):
    baseURL = 'https://api.telegram.org/bot6886102500:AAE7Tj0KHd39kJYcHFQ5hNoHvfPi3Db8x6U/'
    res = req.urlopen(baseURL+command)
    result = json.loads(res.read())['result']
    return result

def sendMessage(chat_id, text):
    query = parse.urlencode([
      ('chat_id', chat_id),
      ('text', text)
    ])
    #print (query)
    baseRequest('sendMessage?'+query)
    
@app.route('/')
def hello_world():
    return 'Flask Telegram Bot Webhook'

@app.route('/6886102500:AAE7Tj0KHd39kJYcHFQ5hNoHvfPi3Db8x6U', methods=['POST','GET'])
def telegram():
    data = request.get_json()
    #print (data)
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    sendMessage(chat_id, text)
    return json.dumps({'success':True})

@app.route('/app')
def app_world():
    return json.encoder({'id': 10 ,'userId': 10 ,'title':'Flask'})