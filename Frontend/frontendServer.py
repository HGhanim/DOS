from flask import Flask
import requests

CATALOG_IP = 'http://192.168.1.207:5000'
ORDER_IP = 'http://192.168.1.35:5000'

frontend_server = Flask(__name__)

@frontend_server.route('/search/<string:subject>', methods = ['GET'])
def search(subject):
    try:
        response = requests.get(CATALOG_IP + '/search/' + subject)
        return response.json(), response.status_code
    except:
        return {"status": "A server error occured."}, 500

@frontend_server.route('/info/<int:id>', methods = ['GET'])
def info(id):
    try:
        response = requests.get(CATALOG_IP +'/info/' + str(id))
        return response.json(), response.status_code
    except:
        return {"status": "A server error occured."}, 500

@frontend_server.route('/purchase/<int:id>', methods = ['PUT'])
def purchase(id):
    try:
        response = requests.put(ORDER_IP + '/purchase/' + str(id))
        return response.json(), response.status_code
    except:
        return {"status": "A server error occured."}, 500

def main():
    frontend_server.run(debug=True)

if __name__ == '__main__':
    main()