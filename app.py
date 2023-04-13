import requests
from flask import Flask, redirect, request, render_template, flash
from currencies import Currencies

app = Flask(__name__)
app.config['SECRET_KEY'] = 'showmethemoney'

apiURL = 'https://api.exchangerate.host/'

currencies = Currencies()

@app.route('/')
def show_form_page():
    """Show convert form on home page"""

    if currencies.codes == {}:
        """check if codes list has been made and make if not"""
        response = requests.get(apiURL + "symbols")
        data = response.json()
        codes = data['symbols']
        currencies.make_currency_code_list(codes)

    return render_template('convert.html') # , codes=currencies.codes)

@app.route('/convert')
def convert():
    """show converted currency"""

    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')

    response = requests.get(apiURL + f'convert?places=2&from={from_currency}&to={to_currency}&amount={amount}')
    data = response.json()
    result = "{:,.2f}".format(data['result'])

    formatted_amount = "{:,.2f}".format(int(amount))

    return render_template('converted.html', result=result, from_curr=from_currency, amount=formatted_amount, to_curr=to_currency)

@app.route('/check-values')
def check_values():
    """check validity of form values"""

    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')

    from_pass = currencies.check_valid(from_currency)
    to_pass = currencies.check_valid(to_currency)
    amount_pass = currencies.check_if_num(amount)

    if from_pass == False:
        flash(f'{from_currency} is not a valid currency')
    if to_pass == False:
        flash(f'{to_currency} is not a valid currency')
    if amount_pass == False:
        flash(f'{amount} is not a valid number')
    if from_pass and to_pass and amount_pass == True:
        return redirect(f'/convert?from={from_currency}&to={to_currency}&amount={amount}')
    
    return redirect('/')
