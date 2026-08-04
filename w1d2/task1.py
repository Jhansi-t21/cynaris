import pandas as pd
import os

print("=" * 60)
print("PANDAS DATA MANIPULATION")
print("=" * 60)

# 1. Load Dataset
print("\n1. Loading Dataset...")

df = pd.read_csv("Districts.csv")   # Change filename if needed

print("Dataset Loaded Successfully!")

# 2. Shape
print("\n2. Shape of Dataset")
print(df.shape)

# 3. Data Types
print("\n3. Data Types")
print(df.dtypes)

# 4. First 10 Rows
print("\n4. printing the first 10 Rows")
print(df.head(10))

# 5. Filter
print("\n5. Districts with Literacy greater than 80")

filtered_df = df[df["Literacy"] > 80]

print(filtered_df)

# 6. GroupBy
print("\n6. Average Literacy State-wise")

grouped_df = df.groupby("State")["Literacy"].mean()

print(grouped_df)

# 7. Merge

print("\n7. Merge Example")

region_df = pd.DataFrame({
    "State": [
        "Karnataka",
        "Maharashtra",
        "Tamil Nadu",
        "Kerala",
        "West Bengal",
        "Bihar",
        "Uttar Pradesh",
        "Gujarat",
        "Delhi",
        "Rajasthan",
        "Andhra Pradesh",
        "Punjab",
        "Chhattisgarh",
        "Madhya Pradesh",
        "Orissa"
    ],
    "Region": [
        "South",
        "West",
        "South",
        "South",
        "East",
        "East",
        "North",
        "West",
        "North",
        "North",
        "South",
        "North",
        "Central",
        "Central",
        "East"
    ]
})

merged_df = pd.merge(df, region_df, on="State", how="left")

print(merged_df.head())

# 8. Pivot Table

print("\n8. Pivot Table - Average Literacy by State")

pivot = pd.pivot_table(
    df,
    values="Literacy",
    index="State",
    aggfunc="mean"
)

print(pivot)

# 9. Export CSV

print("\n9. Exporting Filtered Data to CSV")

filtered_df.to_csv("cleaned_data.csv", index=False)

print("cleaned_data.csv created")

# 10. Export Parquet

print("\n10. Exporting Filtered Data to Parquet")

filtered_df.to_parquet("cleaned_data.parquet", index=False)

print("cleaned_data.parquet created")

# 11. Compare File Sizes

print("\n11. Comparing File Sizes")

csv_size = os.path.getsize("cleaned_data.csv")
parquet_size = os.path.getsize("cleaned_data.parquet")

print("CSV File Size:", csv_size, "bytes")
print("Parquet File Size:", parquet_size, "bytes")

