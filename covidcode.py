import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Creating the dataset
# Let's create some random data for the example
dates = pd.date_range(start='2023-01-01', end='2023-12-31')
confirmed_cases = np.random.randint(100, 1000, size=len(dates))
deaths = np.random.randint(5, 50, size=len(dates))
recovered = np.random.randint(50, 800, size=len(dates))

# Create a DataFrame
covid_data = pd.DataFrame({
    'Date': dates,
    'Confirmed Cases': confirmed_cases,
    'Deaths': deaths,
    'Recovered': recovered
})

# Step 2: Data Visualization
# Plotting confirmed cases, deaths, and recovered over time
plt.figure(figsize=(10, 6))
plt.plot(covid_data['Date'], covid_data['Confirmed Cases'], label='Confirmed Cases', color='blue')
plt.plot(covid_data['Date'], covid_data['Deaths'], label='Deaths', color='red')
plt.plot(covid_data['Date'], covid_data['Recovered'], label='Recovered', color='green')
plt.title('COVID-19 Stats Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()