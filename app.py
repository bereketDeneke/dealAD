import flask
from flask import jsonify
validate = __import__("backend/validate")

app = flask.Flask(__name__)

@app.route('/api/v1/users', methods=['GET', 'POST'])
def getMembers(request):
    if request.method == 'POST':
        if request.json['username'] == 'admin':
            return jsonify({'status':'success'})
        else:
            return jsonify({'status': 'error'})

@app.route('/api/v1/register', methods=['POST'])
def register(request):
    validate.validateInput(request)




