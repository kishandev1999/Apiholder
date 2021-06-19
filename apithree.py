from flask import Flask,request,jsonify
import requests
import pprint
import json
logics =Flask(__name__)
@logics.route('/', methods = ['GET','POST'])
def collect():
    data_req = request.get_json()
    name = data_req['name']
    age= data_req['age']
    random = data_req['random']
    
    payload = json.dumps({"name":str(name),"age":int(age),"random":int(random)})
    
    headers = {"Content-Type": "application/json"}
    
    response = requests.request("POST",'http://127.0.0.1:5001/',headers=headers,data=payload)
    
    
    next_input =json.loads(response.text)
    random=next_input['output']
    payload2 =json.dumps({"random":int(random)})
    response2=requests.request("POST",'http://127.0.0.1:5002/',headers=headers,data=payload2)
    
    
    f_output = json.loads(response2.text)
    return (jsonify({"final_out":f_output['output']}))

if __name__ == '__main__':
    logics.run(debug=True,port=5003)