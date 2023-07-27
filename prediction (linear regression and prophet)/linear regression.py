import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Load the historical cryptocurrency
# ？？？？ do i get this data from api 
data = pd.read_csv('crypto_prices.csv')
#days = input , here is for how many days will I 

# Assuming api will have two columns: 'Timestamp' and 'Price'
timestamps = data['Timestamp']
prices = data['Price']

# Step 2: Prepare the data
# Convert timestamps to numeric values (days, seconds, or any other unit)
timestamps = pd.to_numeric(timestamps)

# Step 3: Split the data into training and testing sets
train_timestamps, test_timestamps, train_prices, test_prices = train_test_split(timestamps, prices, test_size=0.2, random_state=42)

# Step 4: Create a linear regression model
model = LinearRegression()

# Step 5: Train the model using the training data
train_timestamps = np.array(train_timestamps).reshape(-1, 1)  # Reshape to a 2D array
train_prices = np.array(train_prices)
model.fit(train_timestamps, train_prices)

# Step 6: Make predictions using the testing data
test_timestamps = np.array(test_timestamps).reshape(-1, 1)  # Reshape to a 2D array
predictions = model.predict(test_timestamps)


# Step 3: Create a Prophet model and fit it to the data
model = Prophet()
model.fit(data)

# Step 4: Create a dataframe with future timestamps for prediction
future = model.make_future_dataframe(periods=days)  # Predict for the next x days

# Step 5: Make predictions using the Prophet model
forecast = model.predict(future)