from flask import Flask, render_template, request, url_for, redirect, jsonify
from datetime import datetime, timedelta
from random import randint

app = Flask(__name__)
all_orders = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    if request.method == 'POST':
        for key in request.form:
            if request.form[key] == '':
                return render_template('order.html', error='Не все поля заполнены!')
            if key == 'email':
                if not re.match('\\w+@\\w+\\.(ru|com)', request.form[key]):
                    return render_template('order.html', error='Неправильный формат почты')
            if key == 'phone_number':
                if not re.match('\\+7\\d{9}', request.form[key]):
                    return render_template('order.html', error='Неправильный формат номера телефона')
        all_orders.append(request.form)

    return render_template('order.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/lootbox')
def loutbox():
    num= randint(1,100)
    if num < 50: 
        chance = 50 
    elif num > 50 and num < 95: 
        chance = 45 
    elif nu > 95 and num < 99: 
        chance = 4 
    else: 
        chance = 1
    return render_template('lootbox.html',chance=chance)
    


@app.route('/product1')
def product1():
    num= randint(1,10)
    date = datetime.strptime('2022.08.18', '%Y.%m.%d')
    diff = date - datetime.now()
    diff = diff.days
    return render_template('product1.html', action_name='Весенние скидки!', end_date=diff, lucky_num=num)
@app.route('/product2')
def product2():
    return render_template('product2.html')

if __name__ == "__main__":
    app.run()