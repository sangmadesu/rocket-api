from flask import Flask, request, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'rocket-api'
app.config['MONGO_URI'] = 'mongodb://admin:admin123@ds147964.mlab.com:47964/rocket-api'

mongo = PyMongo(app)


# READ
@app.route('/products')
def viewProducts():
    products = mongo.db.products
    output = []

    for product in products.find():
        _id = str(product.get('_id'))
        output.append({'id':_id, 'title':product['title'], 'description':product['description'], 'price':product['price'], 'stock':product['stock']})

    return jsonify(Products = output)

# CREAD

# UPDATE

# DELETE


app.run(debug=True, host='0.0.0.0', port=5000)


