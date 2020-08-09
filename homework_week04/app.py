from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    order_name = request.form['order_name']
    order_count = request.form['order_count']
    order_address = request.form['order_address']
    order_phone = request.form['order_phone']

    db.order.insert_one({'order_name': order_name,
                         'order_count': order_count,
                         'order_address': order_address,
                         'order_phone': order_phone})
    return jsonify({'result': 'success', 'msg': '저장이 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.order.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
