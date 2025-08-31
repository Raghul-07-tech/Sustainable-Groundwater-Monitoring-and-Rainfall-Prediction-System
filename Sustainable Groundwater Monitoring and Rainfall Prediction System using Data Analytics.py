import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# -------------------------------
# Step 1: Load dataset
# -------------------------------
file_path = r"C:\Users\moort\Downloads\state-groundwater-boards-changes-in-depth-to-water-level.csv"
data = pd.read_csv(file_path)

print("First 5 rows of dataset:\n", data.head())
print("\nDataset Info:")
print(data.info())
print("\nMissing values count:\n", data.isnull().sum())

# -------------------------------
# Step 2: Handle missing values
# -------------------------------
for col in data.columns:
    if data[col].dtype == 'object':
        data[col] = data[col].fillna(data[col].mode()[0])   # categorical → mode
    else:
        data[col] = data[col].fillna(data[col].mean())      # numerical → mean

print("\nMissing values after cleaning:\n", data.isnull().sum())

# -------------------------------
# Step 3: Remove duplicates
# -------------------------------
before = data.shape[0]
data = data.drop_duplicates()
after = data.shape[0]
print(f"\nRemoved {before - after} duplicate rows.")

# -------------------------------
# Step 4: Encode categorical columns
# -------------------------------
data_encoded = pd.get_dummies(data, drop_first=True)

# -------------------------------
# Step 5: Normalize numeric columns
# -------------------------------
scaler = MinMaxScaler()
numeric_cols = data_encoded.select_dtypes(include=['float64', 'int64']).columns
data_encoded[numeric_cols] = scaler.fit_transform(data_encoded[numeric_cols])

# -------------------------------
# Step 6: Visualization
# -------------------------------
if 'currentlevel' in data.columns:
    plt.hist(data['currentlevel'].dropna(), bins=30, edgecolor='black')
    plt.xlabel("Current Groundwater Level")
    plt.ylabel("Frequency")
    plt.title("Distribution of Groundwater Level")
    plt.show()

# -------------------------------
# Step 7: Save Cleaned Data
# -------------------------------
output_path = r"C:\Users\moort\Downloads\cleaned_groundwater_data.csv"
data_encoded.to_csv(output_path, index=False)

print(f"\n✅ Preprocessing Completed. Cleaned dataset saved at: {output_path}")
