from flask import Flask,request,jsonify
api2 =Flask(__name__)
@api2.route('/', methods = ['POST'])
def datatwo():
    ran_req=request.get_json()
    random =ran_req['random']
    output2 = random/2
    return (jsonify({'output':output2}))
    #return output2

if __name__ == '__main__':
    api2.run(debug=True,port=5002)