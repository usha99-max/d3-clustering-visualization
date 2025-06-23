import pandas as pd

# Read the XLS file
df = pd.read_excel("cars_dataset.xls")

# Save as CSV
df.to_csv("cars_dataset.csv", index=False)
