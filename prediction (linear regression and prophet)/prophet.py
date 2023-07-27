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

# Prophet requires the columns to be named 'ds' for timestamps and 'y' for the target variable (price)
data = data.rename(columns={'Timestamp': 'ds', 'Price': 'y'})

# Step 3: Create a Prophet model and fit it to the data, prophet already trained the data for us and not need to split that between training and testing 
model = Prophet()
model.fit(data)

# Step 4: Create a dataframe with future timestamps for prediction
future = model.make_future_dataframe(periods=365)  # Predict for the next 365 days

# Step 5: Make predictions using the Prophet model
forecast = model.predict(future)

# Step 6: Visualize the results
model.plot(forecast)
plt.xlabel('Timestamp')
plt.ylabel('Price')
plt.title('Cryptocurrency Price Forecast')
plt.show()