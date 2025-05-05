import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts'

tables = pd.read_html(URL) # goes to url, looks for <table> tags in html, parses each table into a Pandas DataFrame, returns all those tables as a python list or DataFrame

# for future reference: table_dicts = [df.to_dict(orient="records") for df in tables] 
#                          ^ this code will save dataframe as dicts

with open("instagram_tables.txt", "w", encoding="utf-8") as f:
    for i, table in enumerate(tables):
        f.write(f"--- Table {i + 1} ---\n")
        f.write(table.to_string(index=False))
        f.write("\n\n")

data = tables[1]
# data.columns - accesses column names (from source url)
data.columns = ['username', 'name', 'followers', 'profession', 'country', 'unnamed'] # renames data.columns

# .drop - drops/deletes columns
data = data.drop(columns='unnamed')

# .to_dict() turns DataFrame to 
data_list = data.to_dict(orient='records')
data_list.pop() # removes some bs from wikipedias table



