import flask
from flask import jsonify
from flask import render_template
validate = __import__("backend/validate")

app = flask.Flask(__name__)
DOMAIN = "dealAD"

@app.route(f'{DOMAIN}/createSell/', methods=['GET'])
def getMembers(request):
    return render_template("createsellPost.html", request)

@app.route('/api/v1/register', methods=['POST'])
def register(request):
    validate.validateInput(request)




