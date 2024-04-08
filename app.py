from flask import Flask,request
import json
import urllib.parse as parse
import urllib.request as req

app = Flask(__name__)

def baseRequest (command="getMe"):
    baseURL = 'https://api.telegram.org/bot7177567985:AAEz1ydSDfXu3vIgz0UMQ-4wRgmtm4h0Pnc/'
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
    return 'hi~~'

@app.route('/7177567985:AAEz1ydSDfXu3vIgz0UMQ-4wRgmtm4h0Pnc', methods=['POST','GET'])
def telegram():
    data = request.get_json()
    #print (data)
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    sendMessage(chat_id, text)
    return json.dumps({'success':True})
