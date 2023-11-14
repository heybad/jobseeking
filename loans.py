import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the pre-trained model and data
model = LinearRegression()

df = pd.read_csv('data_csv/clean_train.csv')
df = df [['Gender','Married','ApplicantIncome' , 'Education']].dropna()

x = df[['Gender','Married', 'Education']].values
y = df['ApplicantIncome'].values
model.fit(x, y)

def predict_loans (Gender, Married, Education):
  prediction = model.predict([[Gender, Married, Education]])
  return prediction