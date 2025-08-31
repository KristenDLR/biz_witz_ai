from modules.data_loader import load_and_clean

df = load_and_clean("data/sales_data.csv")

print("Data loaded successfully!")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())
