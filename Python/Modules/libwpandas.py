# import sys

# sys.path.append("/home/z/.local/lib/python3.12/site-packages")


import pandas as pd


data = [["a", 1], ["b", 2], ["c", 3]]

df = pd.DataFrame(data)

df.to_csv("abc.csv", header=False, index=False)
