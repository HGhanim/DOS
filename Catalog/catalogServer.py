from flask import Flask
import pandas as pd

catalog_server = Flask(__name__)
#search endpoint
@catalog_server.route('/search/<string:subject>', methods = ['GET'])
def search(subject):
    #read csv file
    catalog = pd.read_csv('catalog_file.csv')
    #get the related data
    data = catalog.loc[catalog['subject'] == subject]
    #check if the books with the subject exist
    if(data.size == 0):
        return {'status' : 'No books with this subject were found.'}, 404
    else:
        #create dataframe
        dataFrame = pd.DataFrame(data, columns = ['id','title'])
        json = dataFrame.to_json(orient = "records")
        #return the books
        return {'data': json}, 200

#info endpoint
@catalog_server.route('/info/<int:id>', methods = ['GET'])
def info(id):
    #read csv file
    catalog = pd.read_csv('catalog_file.csv')
    #get the related data
    data = catalog.loc[catalog['id'] == id]
    #check if the book exists
    if(data.size == 0):
        return {'status' : 'Book not found.'}, 404
    else:
        #create dataframe
        dataFrame = pd.DataFrame(data, columns = ['title','quantity', 'price'])
        json = dataFrame.to_json(orient = "records")
        #return the book
        return {'data': json}, 200
    
#update endpoint
@catalog_server.route('/update/<int:id>', methods = ['PUT'])
def update(id):
    #read csv file
    catalog = pd.read_csv('catalog_file.csv')
    #get the related data
    data = catalog.loc[catalog['id'] == id]
    #decrement the book quantity 
    catalog.loc[data.index , 'quantity'] = catalog['quantity'] - 1
    catalog.to_csv('catalog_file.csv', index = False)
    #return the status of the purchase operation
    return {'status': catalog['title'][id - 1] + ' was bought successfully.'}, 200


def main():
    catalog_server.run(debug=True)

if __name__ == '__main__':
    main()