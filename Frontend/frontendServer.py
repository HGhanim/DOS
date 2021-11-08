from flask import Flask
import requests

frontend_server = Flask(__name__)

@frontend_server.route('/search/<string:subject>', methods = ['GET'])
def search(subject):
    return requests.get('http://192.168.1.207:5000/search/' + subject).json()

@frontend_server.route('/info/<int:id>', methods = ['GET'])
def info(id):
    return requests.get('http://192.168.1.207:5000/info/' + str(id)).json()

@frontend_server.route('/purchase/<int:id>', methods = ['PUT'])
def purchase(id):
    return requests.put('http://192.168.1.35:5000/purchase/' + str(id)).json()

def main():
    frontend_server.run(debug=True)

if __name__ == '__main__':
    main()