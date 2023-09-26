from flask import Flask, jsonify, request
import json

# Dados de exemplo
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

# Criar a instância do aplicativo Flask
app = Flask(__name__)

# Decorator e função para retornar todos os pedidos
@app.route('/purchase_orders', methods=['GET'])
def get_purchase_orders():
    # Retorna todos os pedidos em formato JSON
    return jsonify(purchase_orders)

# Decorator e função para retornar um item específico por ID
@app.route('/purchase_orders_items/<int:item_id>', methods=['GET'])
def get_purchase_orders_items(item_id):
    for order in purchase_orders:
        for item in order['items']:
            if item['id'] == item_id:
                # Retorna o item específico em formato JSON
                return jsonify(item)
    # Se o item não for encontrado, retorna uma mensagem
    return jsonify({'message': 'Item not found'})

# Decorator e função para retornar um pedido específico por ID
@app.route('/purchase_orders_by_id/<int:id>', methods=['GET'])
def get_purchase_orders_by_id(id):
    for order in purchase_orders:
        if order['id'] == id:
            # Retorna o pedido específico em formato JSON
            return jsonify(order)
    # Se o pedido não for encontrado, retorna uma mensagem
    return jsonify({'message': 'Order not found'})

# Decorator e função para adicionar um novo pedido
@app.route('/purchase_orders', methods=['POST'])
def post_purchase_orders_items():
    request_data = request.get_json()
    new_purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'items': []
    }
    
    # Verifica se já existe um pedido com o mesmo ID
    for order in purchase_orders:
        if order['id'] == request_data['id']:
            # Se o pedido com o mesmo ID já existe, retorna uma mensagem de erro
            return jsonify({'message': 'Order with the same ID already exists'})

    # Se nenhum pedido com o mesmo ID for encontrado, adiciona o novo pedido
    purchase_orders.append(new_purchase_order)
    
    # Retorna o novo pedido em formato JSON
    return jsonify(new_purchase_order)

# Iniciar o aplicativo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
