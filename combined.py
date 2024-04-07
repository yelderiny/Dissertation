import pandas as pd

# Assuming your CSV files are named file1.csv, file2.csv, and file3.csv
file_paths = ['/Users/yelderiny/Projects/Dissertation/Data/project-data3.csv',
              '/Users/yelderiny/Projects/Dissertation/Data/project-data3-2.csv']

# Initialize an empty list to store individual DataFrames
dfs = []

# Loop through each file and append its data to the dfs list
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

# Combine all DataFrames in the dfs list into one DataFrame
combined_data = pd.concat(dfs, ignore_index=True)

# Remove duplicates based on the "id" column and keep the first occurrence
combined_data = combined_data.drop_duplicates(subset='name', keep='first')

# Save the combined and deduplicated data to a new CSV file
combined_data.to_csv('/Users/yelderiny/Projects/Dissertation/Data/project-data3.csv', index=False)

# Display information about the combined DataFrame
print("Combined and deduplicated data:")
print(combined_data.head())