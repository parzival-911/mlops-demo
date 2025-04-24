#model.py
from sklearn.linear_model import LinearRegression
import numpy as np

# Training data (simple numbers)
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict the value for input 5
predicted = model.predict([[5]])
print("Prediction for input 5 is:", predicted[0])
