from flask import Flask
import pandas as pd
import requests
import json

order_server = Flask(__name__)

@order_server.route('/purchase/<int:id>')
def purchase(id):
    info = requests.get('http://192.168.1.207:5000/info/'+str(id)).json()
    book = json.loads(info['data'])[0]
    if(book['quantity'] > 0):
        order = {
            'id' : id,
           'title'   : [book['title']],
           'price'   : [book['price']]
           }
        orderDataFrame = pd.DataFrame(order)
        orderDataFrame.to_csv('orders_file.csv', mode='a', index=False, header=False)
        catalogResponse = requests.put('http://192.168.1.207:5000/update/' + str(id)).json()
        return catalogResponse
    else:
        return {'status': book['title'] + ' is out of stock.'}

def main():
    order_server.run(debug=True)

if __name__ == '__main__':
    main()