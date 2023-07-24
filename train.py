import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

# Assuming 'data' is the dataset containing the cement mixture data
data = pd.read_csv('cement_data.csv')

# Handling missing values
data.fillna(data.mean(), inplace=True)

# Normalizing features
scaler = MinMaxScaler()
data[['Water-to-Cement Ratio', 'Compressive Strength (MPa)']] = scaler.fit_transform(data[['Water-to-Cement Ratio', 'Compressive Strength (MPa)']])

# Assuming 'X' contains the input features and 'y' contains the target variable
X = data[['Water-to-Cement Ratio']]
y = data['Compressive Strength (MPa)']

# Creating and training the model
model = LinearRegression()
model.fit(X, y)

#save the trained model
pickle.dump(model, open('model.pkl','wb'))

