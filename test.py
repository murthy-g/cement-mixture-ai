from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle
import pandas as pd

# Assuming 'data' is the dataset containing the cement mixture data
data = pd.read_csv('test_data.csv')

#load the trained model and predict
model = pickle.load(open('model.pkl','rb'))
# print(model.predict([[0.5]]))

# Assuming 'X' contains the input features and 'y' contains the target variable
X = data[['Water-to-Cement Ratio']]
y = data['Compressive Strength (MPa)']


# Model evaluating
y_pred = model.predict(X)

mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Threshold to consider the mixture as "correct"
threshold = 0.5  # Adjust this threshold based on your requirements

# Check if the mixture is "correct" or "not correct" based on the predicted compressive strength
data['Mixture Status'] = ['Correct' if pred_strength >= threshold else 'Not Correct' for pred_strength in y_pred]

# Display the updated DataFrame with the mixture status
data.to_csv('predicted_cement_data.csv', index=False)