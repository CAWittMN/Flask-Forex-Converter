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
    check = session.get('success')
    if check != True:
        flash('Please completely fill out the form')
        return redirect('/')

    f_currency = session['from']
    t_currency = session['to']
    amount = session['amount']

    response = requests.get(apiURL + f'convert?places=2&from={f_currency}&to={t_currency}&amount={amount}')
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

    from_pass = currencies.check_valid(from_currency, codes)
    to_pass = currencies.check_valid(to_currency, codes)
    amount_pass = currencies.check_if_num(amount)

    if from_pass == False:
        flash(f'{from_currency} is not a valid currency')
    if to_pass == False:
        flash(f'{to_currency} is not a valid currency')
    if amount_pass == False:
        flash(f'{amount} is not a valid number')

    if from_pass and to_pass and amount_pass == True:
        session['from'] = str.upper(from_currency)
        session['to'] = str.upper(to_currency)
        session['amount'] = amount
        session['success'] = True
        return redirect('/converted')
    
    return redirect('/')
