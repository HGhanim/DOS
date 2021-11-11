from flask import Flask
import pandas as pd
import requests
import json

#CHANGE THIS TO YOUR CATALOG IP ADDRESS
CATALOG_IP = 'http://192.168.1.207:5000'

order_server = Flask(__name__)

#purchase endpoint
@order_server.route('/purchase/<int:id>', methods = ['PUT'])
def purchase(id):
    #get info about the book
    info = requests.get(CATALOG_IP + '/info/'+str(id)).json()
    #check if the book exitsts
    try:
        book = json.loads(info['data'])[0]
    except:
        return {"status": "Book not found."}, 404
    #check the quantity of the book
    if(book['quantity'] > 0):
        order = {
            'id' : id,
           'title'   : [book['title']],
           'price'   : [book['price']]
           }
        #create dataframe with the book information
        orderDataFrame = pd.DataFrame(order)
        #add the dataframe to the orders
        orderDataFrame.to_csv('orders_file.csv', mode='a', index=False, header=False)
        #send request to catalog server to update the quantity of the book
        catalogResponse = requests.put(CATALOG_IP + '/update/' + str(id)).json()
        #return the response
        return catalogResponse, 200
    else:
        #return 404 message if the book is not available in the stock
        return {'status': book['title'] + ' is out of stock.'}, 404

def main():
    order_server.run(debug=True)

if __name__ == '__main__':
    main()