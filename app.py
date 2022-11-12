import flask
from flask import jsonify, render_template
validate = __import__("backend/validate")

app = flask.Flask(__name__)

# [Begin] Absera
@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")
# [End] Absera

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




