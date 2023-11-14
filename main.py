# main.py
from flask import Flask, render_template, request
from income import predict_income
from loans import predict_loans
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('main.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/portfolio/income', methods=['GET', 'POST'])
def predict_income_route():
    prediction = None
    if request.method == 'POST':
        age = float(request.form['age'])
        experience = float(request.form['experience'])
        prediction = predict_income(age, experience)
    return render_template('income.html', prediction=prediction)





@app.route('/portfolio/loans', methods=['GET', 'POST'])
def loans_route():
    prediction = None
    if request.method == 'POST':
        Gender = request.form['Gender']
        Married = request.form['Married']
        Education = request.form['Education']
        prediction = predict_loans(float(Gender), float(Married), float(Education))
    return render_template('loans.html', prediction=prediction)







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
