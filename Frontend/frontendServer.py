from flask import Flask
import requests

#CHANGE THIS TO YOUR CATALOG IP ADDRESS
CATALOG_IP = 'http://192.168.1.207:5000'
#CHANGE THIS TO YOUR ORDER IP ADDRESS
ORDER_IP = 'http://192.168.1.35:5000'

frontend_server = Flask(__name__)
#search endpoint
@frontend_server.route('/search/<string:subject>', methods = ['GET'])
def search(subject):
    try:
        #send request to catalog server
        response = requests.get(CATALOG_IP + '/search/' + subject)
        #return response
        return response.json(), response.status_code
    except:
        #return response with 500 status
        return {"status": "A server error occured."}, 500
#info endpoint
@frontend_server.route('/info/<int:id>', methods = ['GET'])
def info(id):
    try:
        #send request to catalog server
        response = requests.get(CATALOG_IP +'/info/' + str(id))
        #return response
        return response.json(), response.status_code
    except:
        #return response with 500 status
        return {"status": "A server error occured."}, 500
#purchase endpoint
@frontend_server.route('/purchase/<int:id>', methods = ['PUT'])
def purchase(id):
    try:
        #send request to order server
        response = requests.put(ORDER_IP + '/purchase/' + str(id))
        #return response
        return response.json(), response.status_code
    except:
        #return response with 500 status
        return {"status": "A server error occured."}, 500

def main():
    frontend_server.run(debug=True)

if __name__ == '__main__':
    main()