from flask import Flask,request
import json
import urllib.parse as parse
import urllib. request as req
app = Flask(__name__)
def baseRequest (command="getMe"):
    baseURL = 'https://api.telegran.org/bot7050846499:AAEs_EPADdydBPcggtKpQSpXLCLNebIeG3o'
    res = req.urlopen(baseURL+command)
    result = json.loads(res.read())['result']
    return result
def sendMessage(chat_id, text):
    query = parse. urlencode([
    ('chat_id', chat_id),
    ('text', text)
    ]}
    #print (query)
    baseRequest('sendMessage?'+query)
    
@app.route("/")
def hello_world(): :
    return 'hi'

@app.route("/937911760:AMGoaceL_hvdr3viab1dBiofapXHpOLRSHA", methods=[ 'POST', 'GET'])
def telegran():
    data = request.get_json()
    print (data)
    chat_id = data ['message']['chat']['id']
    text = data['message']['text']
    sendMessage(chat_id, text)
    return json.dumps ({success':True})
