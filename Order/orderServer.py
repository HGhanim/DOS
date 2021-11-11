from flask import Flask
import pandas as pd
import requests
import json

CATALOG_IP = 'http://192.168.1.207:5000'

order_server = Flask(__name__)

@order_server.route('/purchase/<int:id>', methods = ['PUT'])
def purchase(id):
    info = requests.get(CATALOG_IP + '/info/'+str(id)).json()
    try:
        book = json.loads(info['data'])[0]
    except:
        return {"status": "Book not found."}, 404
    if(book['quantity'] > 0):
        order = {
            'id' : id,
           'title'   : [book['title']],
           'price'   : [book['price']]
           }
        orderDataFrame = pd.DataFrame(order)
        orderDataFrame.to_csv('orders_file.csv', mode='a', index=False, header=False)
        catalogResponse = requests.put(CATALOG_IP + '/update/' + str(id)).json()
        return catalogResponse, 200
    else:
        return {'status': book['title'] + ' is out of stock.'}, 404

def main():
    order_server.run(debug=True)

if __name__ == '__main__':
    main()