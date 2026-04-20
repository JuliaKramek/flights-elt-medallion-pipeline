import pandas as pd

print("Starting Silver layer")

df = pd.read_csv("/opt/project/archive-2/travelverse-dataset.csv")

df = df.drop_duplicates()

df.to_parquet("/opt/project/silver/output", index=False)

print("Silver completed")
