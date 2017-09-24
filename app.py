from flask import Flask, request, jsonify, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'rocket-api'
app.config['MONGO_URI'] = 'mongodb://admin:admin123@ds147964.mlab.com:47964/rocket-api'

mongo = PyMongo(app)


# Error Handler
# @app.errorhandler(500)
# def catch_server_error(e):
#     return jsonify({"info":"Something went wrong!"})


# CREATE
@app.route('/products', methods=['POST'])
def addProducts():
    products = mongo.db.products
    title = request.json['title']
    description = request.json['description']
    price = request.json['price']
    stock = request.json['stock']

    try:
        insert_product = products.insert({'title':title, 'description':description, 'price':price, 'stock':stock})
        print(insert_product)

        return jsonify({"info": "Created product success!"})
    except Exception as e:
        print(e)
        
        return abort(500)


# READ
@app.route('/products')
def viewAllProducts():
    products = mongo.db.products
    output = []

    for product in products.find():
        _id = str(product.get('_id'))
        output.append({'id':_id, 'title':product['title'], 'description':product['description'], 'price':product['price'], 'stock':product['stock']})

    return jsonify(output)

        
# VIEW
@app.route('/products/<id>')
def viewProduct(id):
    print(id)
    products = mongo.db.products
    try:
        product = products.find_one({'_id':ObjectId(id)})
        output = {'_id':str(product.get('_id')), 'title':product.get('title'), 'description':product.get('description'), 'price':product.get('stock')}

        return jsonify(output)
    except Exception as e:
        raise e
        print(e)

        return abort(500)


# UPDATE

# DELETE


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)



