import requests
from flask import Flask, redirect, request, render_template, flash, session
from currencies import Currencies

app = Flask(__name__)
app.config['SECRET_KEY'] = 'showmethemoney'

apiURL = 'https://api.exchangerate.host/'

currencies = Currencies()

@app.route('/')
def show_form_page():
    """Show convert form on home page"""
    session['codes'] = session.get('codes', {})
    session['success'] = session.get('success', False)
    if session['codes'] == {}:
        """check if codes list has been made and make if not"""
        response = requests.get(apiURL + "symbols")
        data = response.json()
        codes = data['symbols']
        session['codes'] = codes

    return render_template('convert.html') # , codes=session['codes'])

@app.route('/converted')
def convert():
    """show converted currency"""

    """check if the form had been filled out succesfully"""
    check_complete = session.get('success', False)
    if check_complete != True:
        flash('Please completely fill out the form')
        return redirect('/')

    from_currency = session['from']
    to_currency = session['to']
    amount = session['amount']

    response = requests.get(apiURL + f'convert?places=2&from={from_currency}&to={to_currency}&amount={amount}')
    data = response.json()
    result = "{:,.2f}".format(data['result'])

    session['amount'] = "{:,.2f}".format(float(amount))
    session['result'] = result


    return render_template('converted.html', result=result)

@app.route('/check-values', methods=['POST'])
def check_values():
    """check validity of form values and save to session"""

    from_currency = request.form.get('from')
    to_currency = request.form.get('to')
    amount = request.form.get('amount')
    codes = session.get('codes',{})

    from_is_valid = currencies.check_valid(from_currency, codes)
    to_is_valid = currencies.check_valid(to_currency, codes)
    amount_is_valid = currencies.check_if_num(amount)

    if from_is_valid == False:
        flash(f'{from_currency} is not a valid currency')
    if to_is_valid == False:
        flash(f'{to_currency} is not a valid currency')
    if amount_is_valid == False:
        flash(f'{amount} is not a valid number')

    if from_is_valid and to_is_valid and amount_is_valid == True:
        session['from'] = str.upper(from_currency)
        session['to'] = str.upper(to_currency)
        session['amount'] = amount
        session['success'] = True
        return redirect('/converted')
    
    return redirect('/')
