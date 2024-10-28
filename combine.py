
import pandas as pd
import glob
import os

# Get all CSV files in the data directory
path = "data"
all_files = [f for f in glob.glob(os.path.join(path, "*.csv")) if not f.endswith("output.csv")]

# Create empty list to store dataframes
df_list = []

# Read first CSV file and keep only first row
if all_files:
    df = pd.read_csv(all_files[0])
    df = df.head(1)
    df_list.append(df)

# Read each CSV file and append to list
for filename in all_files:
    df = pd.read_csv(filename)
    df_list.append(df)

# Combine all dataframes
combined_df = pd.concat(df_list, ignore_index=True)

# Remove existing combined.csv if it exists
if os.path.exists("data/combined.csv"):
    os.remove("data/combined.csv")

# Write combined dataframe to CSV
combined_df.to_csv("data/combined.csv", index=False)
