from flask import Flask, render_template


app = Flask(__name__)


# https://www.domena.hr/
@app.route('/')
def index():
    return render_template('index.html')


# https://www.domena.hr/customers
@app.route('/customers')
def customers():
    return render_template('customers.html')




if __name__ == '__main__':
    app.run(debug=True)
