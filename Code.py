
# Importing the necessary libraries for data simulation and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a random seed for reproducibility
np.random.seed(42)

# Simulating 50 years of CO2 emissions and global temperature rise data
years = np.arange(1970, 2020)
co2_emissions = np.linspace(3000, 40000, len(years))  # Simulating a steady rise in CO2 emissions (in MtCO2)
temperature_rise = 0.02 * (co2_emissions / 1000) + np.random.normal(0, 0.1, len(years))  # Simulated temp increase

# Creating a DataFrame for the data
data = pd.DataFrame({
    'Year': years,
    'CO2 Emissions (MtCO2)': co2_emissions,
    'Global Temperature Rise (°C)': temperature_rise
})

# Plot 1: CO2 emissions over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='CO2 Emissions (MtCO2)', data=data, color="blue", label="CO2 Emissions")
plt.title('Global CO2 Emissions (1970-2020)')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (MtCO2)')
plt.grid(True)
plt.show()

# Plot 2: Global temperature rise over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Global Temperature Rise (°C)', data=data, color="red", label="Temperature Rise")
plt.title('Global Temperature Rise (1970-2020)')
plt.xlabel('Year')
plt.ylabel('Global Temperature Rise (°C)')
plt.grid(True)
plt.show()

# Plot 3: Correlation between CO2 emissions and temperature rise
plt.figure(figsize=(10, 6))
sns.scatterplot(x='CO2 Emissions (MtCO2)', y='Global Temperature Rise (°C)', data=data, color="green")
plt.title('Correlation between CO2 Emissions and Global Temperature Rise')
plt.xlabel('CO2 Emissions (MtCO2)')
plt.ylabel('Global Temperature Rise (°C)')
plt.grid(True)
plt.show()

# Displaying the first few rows of the dataset to review the simulated data
print(data.head())

# Save the dataset as a CSV file for future use
data.to_csv('co2_temperature_simulation.csv', index=False)
