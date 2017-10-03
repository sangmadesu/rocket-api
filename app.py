from flask import Flask, request, jsonify, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from config import dbName, dbUrl


app = Flask(__name__)

app.config['MONGO_DBNAME'] = dbName
app.config['MONGO_URI'] = dbUrl

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
        # print(insert_product)

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
        print(e)

        return abort(500)


# UPDATE
@app.route('/products/<id>', methods=['PUT'])
def updateProduct(id):
    products = mongo.db.products
    data = request.get_json()
    try:
        products.update({'_id': ObjectId(id)}, { "$set": data})

        return jsonify({"info": "Product Updated Successfully"})
    except Exception as e:
        print(e)

        return abort(500)


# DELETE
@app.route('/products/delete/<id>', methods=['DELETE'])
def deleteProduct(id):
    products = mongo.db.products
    # print(id)
    try:
        # pass
        products.remove({'_id': ObjectId(id)})

        return jsonify({"info": "Product Deleted Successfully"})
    except Exception as e:
        pritn(e)

        return abort(500)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)



