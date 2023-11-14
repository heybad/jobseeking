import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the pre-trained model and data
model = LinearRegression()
df = pd.read_csv('data_csv/agevsincome.csv')
x = df[['age', 'experience']].values
y = df[['income']].values
model.fit(x, y)

def predict_income (age, experience):
    prediction = model.predict([[age, experience]])
    return prediction



