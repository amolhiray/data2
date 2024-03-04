from flask import Flask,render_template,url_for,request
from flask import jsonify
from utils import get_predicted_loan_status


app = Flask(__name__)
@app.route('/')
def home(): 

    return render_template ('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Dependents = int(request.form['Dependents'])
    Education = int(request.form['Education'])
    Self_Employed = int(request.form['Self_Employed'])
    ApplicantIncome = float(request.form['ApplicantIncome'])
    CoapplicantIncome = float(request.form['CoapplicantIncome'])
    LoanAmount = float(request.form['LoanAmount'])
    Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
    Credit_History = int(request.form['Credit_History'])
    Property_Area = int(request.form['Property_Area'])
    
    predicted = get_predicted_loan_status(Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
    
    if predicted == 1:
        loan_status= 'Approved'
    else:
        loan_status = 'Not Approved'

    return render_template('index.html',prediction_text=f'Predicted loan status is: {loan_status}')

 
if __name__=='__main__':
     app.run(host='0.0.0.0',port=5010,debug=False)
