from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/')
def hello_world():
   return ('Hello World')
   
@app.route('/super_simple')
def super_simple():
   return jsonify(message ='hello world again from planetary-API'), 200

@app.route('/not_found')
def not_found():
   return jsonify(message='resource not found '), 404

# @app.route('/parameters')
# def parameters():
#    name=request.args.get('name')
#    age = int(request.args.get('age'))
   
#    if age<18:
#       return jsonify(message="Sorry "+ name +", you are not eligible."), 401
#    else:
#       return jsonify(message="Hello "+ name +", Welcome!!")

@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name:str,age:int):
   if age<18:
      return jsonify(message="Sorry "+ name +", you are not eligible."), 401
   else:
      return jsonify(message="Hello "+ name +", Welcome!!")
   
   
if __name__=='__main__':
   app.run()