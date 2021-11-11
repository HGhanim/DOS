from flask import Flask
import pandas as pd

catalog_server = Flask(__name__)

@catalog_server.route('/search/<string:subject>', methods = ['GET'])
def search(subject):
    catalog = pd.read_csv('catalog_file.csv')
    data = catalog.loc[catalog['subject'] == subject]
    if(data.size == 0):
        return {'status' : 'No books with this subject were found.'}, 404
    else:
        dataFrame = pd.DataFrame(data, columns = ['id','title'])
        json = dataFrame.to_json(orient = "records")
        return {'data': json}, 200

@catalog_server.route('/info/<int:id>', methods = ['GET'])
def info(id):
    catalog = pd.read_csv('catalog_file.csv')
    data = catalog.loc[catalog['id'] == id]
    if(data.size == 0):
        return {'status' : 'Book not found.'}, 404
    else:
        dataFrame = pd.DataFrame(data, columns = ['title','quantity', 'price'])
        json = dataFrame.to_json(orient = "records")
        return {'data': json}, 200
    

@catalog_server.route('/update/<int:id>', methods = ['PUT'])
def update(id):
    catalog = pd.read_csv('catalog_file.csv')
    data = catalog.loc[catalog['id'] == id]
    catalog.loc[data.index , 'quantity'] = catalog['quantity'] - 1
    catalog.to_csv('catalog_file.csv', index = False)
    return {'status': catalog['title'][id - 1] + ' was bought successfully.'}, 200


def main():
    catalog_server.run(debug=True)

if __name__ == '__main__':
    main()