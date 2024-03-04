
import pickle
import numpy as np


def get_predicted_loan_status(Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
    file_path = 'logistic.pkl'
     
    with open(file_path,'rb') as file:
        model = pickle.load(file)
    test_array = np.array([[Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])     
    predicted = model.predict(test_array)
    return predicted
          

