from flask import Flask,request,jsonify
api1 =Flask(__name__)
@api1.route('/', methods = ['POST'])
def data():
    data_req =request.get_json()
    name = data_req['name']
    age = data_req['age']
    random = data_req['random']
    output = age+random
    output1=jsonify({"output":output})
    return output1   

if __name__ == '__main__':
    api1.run(debug=True,port=5001)