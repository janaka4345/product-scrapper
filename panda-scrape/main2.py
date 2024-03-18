import pandas as pd

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
print(table[0])