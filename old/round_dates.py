import pandas as pd

# Load the CSV file
file_path = "c:\\Users\\nikol\\OneDrive - OGS\\Projects\\ICOS\\script\\dates.csv"
df = pd.read_csv(file_path)

# Assuming the date column is named 'date', parse it as datetime
df['date'] = pd.to_datetime(df['date'])

# Round the dates to the nearest hour
df['date'] = df['date'].dt.round('H')

# Save the updated DataFrame back to the CSV file
df.to_csv(file_path, index=False)

print("Dates have been rounded to the nearest hour.")