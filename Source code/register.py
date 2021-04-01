
from flask import Flask, request, render_template
from logging import DEBUG


app = Flask(__name__)
app.logger.setLevel(DEBUG)

@app.route('/customer-register.html')
def my_form():
    return render_template('customer-register.html')
@app.route('/customer-register.html', methods=['POST'])
def my_form_post():
    text = request.form['name']
    processed_text = text.upper()
    app.logger.debug('stored feedback obtained: ' + processed_text)
    return render_template('index.html')

app.run(debug='True')

