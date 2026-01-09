import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
hours = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
marks = np.array([10,20,30,40,50,60,70,80,90,100])

# Train model
model = LinearRegression()
model.fit(hours, marks)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved")
