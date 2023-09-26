from flask import Flask, jsonify


purchase_orders = [
    {
    
        'id': 1,
        'description': 'Pedido de compra',
        'items': [
            {
                'id': 1,
                'description': 'Coca-Cola',
                'price': 1.00
            },
        ]
    }
]

# To-Do
# request_methods 
# GET purchase_orders
# POST purchase_orders
# GET purchase_orders_by_id
# GET purchase_orders_items
# POST purchase_orders_items

app = Flask(__name__)

#definindo um decorator purchase_orders
@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)

# Definindo o decorator purchase_orders_by_id
@app.route('/purchase_orders_by_id/<int:id>')

# função que retornar um purchase_order por id
def get_purchase_orders_by_id(id):
    try:
        for order in purchase_orders:  # percorrendo o dicionário de purchase_orders
            if order['id'] == id:   # Comparando se o id informado existe no arrayd e purchase_orders
                return jsonify(order)  
    except Exception as e:
        print(f"Error", e)
    return jsonify({'message': 'Order not found'})

# Definindo o decorator purchase_orders_items
      


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug= True)
    
    
    
    

    
    