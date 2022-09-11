from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
studentDB=[
{   
    'name':'john',
    'rollno':'11',   
},
    {
    'name':'jn',
    'rollno':'171',
}]
@app.route("/",methods=['GET'])
def welcome():
    return "welcome"

@app.route("/student/getStudents",methods=['GET'])
def getStudents():
    return jsonify({"student":studentDB})

if __name__ =="__main__":
    app.run()
