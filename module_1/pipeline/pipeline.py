import sys

try:
    import pandas as pd
except ImportError:
    print("Error: pandas is required. Install with `pip install pandas`.")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Usage: python pipeline.py <month>")
    sys.exit(1)

print("Hello pipeline!")
print("Arguments:", sys.argv)

try:
    month = int(sys.argv[1])
except ValueError:
    print("Error: month must be an integer.")
    sys.exit(1)

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})

df["month"] = month

print(df.head())

df.to_parquet(f"output_day_{month}.parquet")