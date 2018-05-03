from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def ui():
   return render_template('menue.html')


@app.route('/get_order', methods = ['POST'])
def get_order():
        order = {}
        name = request.form['name']
        cibus = request.form['cibus']
        mainDish = request.form['maindish']
        sideDish1 = request.form['side1']
        sideDish2 = request.form['side2']

        order.update({'cibus': cibus, 'name': name, 'main_dish': mainDish, 'side_dish_no.1': sideDish1,
                             'side_dish_no.2': sideDish2})
        print (order)
        with open('{}.json'.format(cibus), 'w') as fp:
            json.dump(order, fp, indent=4, sort_keys=True)

        return render_template('menue.html'), 201


if __name__ == '__main__':
   app.run(host='0.0.0.0')