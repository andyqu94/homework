import pandas as pd 
filepath = "Resources/cities.csv"
df = pd.read_csv(filepath)
data_html = df.to_html("data.html", bold_rows = True)