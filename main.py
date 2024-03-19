from flask import Flask, render_template

from services.rest_api_services.users_api_manager import get_all_users, get_user
from services.rest_api_services.sensors_api_manager import get_temperatures


app = Flask(__name__)


# https://www.domena.hr/
@app.route('/')
def index():
    temperatures = get_temperatures()
    return render_template('index.html', temperatures=temperatures)


# https://www.domena.hr/customers
@app.route('/customers')
def customers():
    users_from_function = get_all_users()
    return render_template('customers.html', users_in_template=users_from_function)


# https://www.domena.hr/customers
@app.route('/customers/<int:id>')
def customer(id):
    user = get_user(id)
    return render_template('customer.html', user=user)




if __name__ == '__main__':
    app.run(debug=True)
