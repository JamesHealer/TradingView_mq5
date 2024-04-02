# from flask import Flask, request, jsonify
# import MetaTrader5 as mt5
# from flask_cors import CORS
# import time

# app = Flask(__name__)
# CORS(app)

# # Initialize MetaTrader5 connection
# mt5.initialize()

# @app.route('/orders', methods=['POST'])
# def receive_orders():
#     if request.method == 'POST':
#         orders = request.json
#         print("Orders received from FrontEnd successful")
#         send_multiple_orders(orders)
#         return jsonify({"message": "Orders received and sent to MT5"}), 200
#     else:
#         return jsonify({'error': 'Method not allowed'}), 405

# def send_order_to_mt5(symbol, action, volume, price):
#     request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": symbol,
#         "volume": volume,
#         "type": mt5.ORDER_TYPE_BUY if action == 'BUY' else mt5.ORDER_TYPE_SELL,
#         "price": price,
#         "deviation": 10,
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }

#     print("Order request:", request)  # Log the order request data

#     # Send the order
#     result = mt5.order_send(request)
#     if result is None:
#         print("Order send failed: result is None")
#         return False

#     if result.retcode != mt5.TRADE_RETCODE_DONE:
#         print("Order send failed, retcode={}".format(result.retcode))
#         print("Error:", result.comment)
#         return False
#     else:
#         print("Order placed successfully")
#         return True

# def send_multiple_orders(orders):
#     for order in orders:
#         success = send_order_to_mt5(order['symbol'], order['side'], order['qty'], order['avg_price'])
#         if success:
#             time.sleep(1)

# if __name__ == '__main__':
#     app.run(debug=True)


import socket
import json

def send_orders_to_ea(orders):
    # Create a socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8888)

    try:
        # Connect to the EA
        client_socket.connect(server_address)
        print("Connected to EA")

        # Send orders to the EA
        for order in orders:
            order_json = json.dumps(order)
            client_socket.sendall(order_json.encode())
            print("Sent order:", order_json)

    except ConnectionRefusedError:
        print("Connection to EA refused")
    finally:
        # Close the socket connection
        client_socket.close()

# Example usage
orders = [
    {"symbol": "EURUSD", "action": "BUY", "volume": 0.1, "price": 1.12345},
    {"symbol": "GBPUSD", "action": "SELL", "volume": 0.2, "price": 1.23456}
]

send_orders_to_ea(orders)
