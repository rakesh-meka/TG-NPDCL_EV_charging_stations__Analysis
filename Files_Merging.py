import pandas as pd
import glob
import os

# Define the folder containing CSV files
folder_path = "D:/Projects/Project - TG NPDCL/"  # Update with your folder path

#  Get all CSV files in the folder
file_list = glob.glob(os.path.join(folder_path, "*.csv"))

# Debugging: Check if June file is in the list
print("Files found:", file_list)  # Ensure June file is included

# Initialize an empty list to store DataFrames
df_list = []

#Merge all CSV files while keeping only the first header
for i, file in enumerate(file_list):
    df = pd.read_csv(file)  # Read CSV file
    if i == 0:
        df_list.append(df)  # Keep header for the first file
    else:
        df_list.append(df.iloc[1:, :])  # Skip header row for subsequent files

#  Combine all DataFrames into one
merged_df = pd.concat(df_list, ignore_index=True)

# Drop rows where "Month" column is missing
merged_df = merged_df.dropna(subset=["Month"])

#Convert "Month" column to datetime format (MMM-YY)
merged_df["Month"] = pd.to_datetime(merged_df["Month"], format="%b-%y", errors="coerce")

# Check for errors in Month conversion
if merged_df["Month"].isna().sum() > 0:
    print("⚠️ Some 'Month' values could not be converted. Check format (MMM-YY).")

#  Sort DataFrame by "Month"
merged_df = merged_df.sort_values(by="Month")

#  Convert back to "MMM-YY" format for readability
merged_df["Month"] = merged_df["Month"].dt.strftime("%b-%y")

# Save the final merged & sorted data to a new CSV file
output_path = os.path.join(folder_path, "final_sorted_output.csv")
merged_df.to_csv(output_path, index=False)

print("Merging & Sorting Completed!", output_path)
