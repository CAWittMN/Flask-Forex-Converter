import requests
from flask import Flask, redirect, request, render_template
from currencies import Currencies

app = Flask(__name__)
app.config['SECRET_KEY'] = 'showmethemoney'

currencies = Currencies()
apiURL = 'https://api.exchangerate.host/'


@app.route('/')
def initiate_home_page():
    if currencies.codes == {}:
        response = requests.get(apiURL + "symbols")
        data = response.json()
        codes = data['symbols']
        currencies.make_currency_code_list(codes)
    return render_template('convert.html', codes=currencies.codes)

@app.route('/convert')
def convert():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')
    if currencies.check_valid(to_currency, from_currency):
        response = requests.get(apiURL + f'convert?places=2&from={from_currency}&to={to_currency}&amount={amount}')
        data = response.json()
        result = "{:,.2f}".format(data['result'])
        formatted_amount = "{:,.2f}".format(int(amount))
        return render_template('converted.html', result=result, from_curr=from_currency, amount=formatted_amount, to_curr=to_currency)
    return redirect('/')