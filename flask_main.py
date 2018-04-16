import random
import requests
from flask import Flask, request, jsonify
app = Flask(__name__)
import os

destination_host ='https://api.telegram.org/'

if not os.path.exists("images"):
    os.makedirs("images")

def get_file_name():
    random_name = os.path.join("images", str(random.randint(0, 100000)) +'.jpg')
    return random_name

def parse_flask_dict(flask_dict):
    exit_dict = {}
    for i in flask_dict:
        exit_dict[i] = flask_dict[i]
    return exit_dict

@app.route('/<path:path>', methods=['GET','POST'])
def main(path):
    content = "HELLO"
    print path
    if 'photo' in request.files:
        file = request.files['photo']
        file.save(get_file_name())
    arguments = parse_flask_dict(request.form)
    if request.method =='GET':
        r = requests.get(destination_host+path)
        return r.json()
    elif request.method =='POST':
        r = requests.post(destination_host+path, data = arguments)
        return r.json()
    else:
        return 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')