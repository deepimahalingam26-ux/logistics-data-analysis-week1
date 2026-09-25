import pandas as pd
import matplotlib.pyplot as plt

# Load logistics dataset
data = pd.read_csv("logistics_data.csv")

# Display basic information
print(data.head())
print(data.info())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove missing values
data = data.dropna()

# Calculate average delivery time
average_time = data["Delivery_Time"].mean()
print("\nAverage Delivery Time:", average_time)

# Calculate On-Time Delivery Rate
on_time = (data["Delivery_Status"] == "On-Time").sum()
total = len(data)

rate = (on_time / total) * 100
print("On-Time Delivery Rate:", rate)

# Visualize delivery time
data["Delivery_Time"].hist()

plt.xlabel("Delivery Time")
plt.ylabel("Number of Deliveries")
plt.title("Delivery Time Distribution")
plt.show()
