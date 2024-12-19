import duckdb
import pandas as pd

queries = [['abxy', 'SELECT * FROM abxy'],
           ['a1b0', 'SELECT * FROM a1b0'],
           ['a1b1', 'SELECT * FROM a1b1']]

conn = duckdb.connect('abxy.duckdb', read_only=True)

with pd.ExcelWriter ('abxy.xlsx', engine='xlsxwriter') as writer:
    for name, query in queries:
        df = conn.execute(query).fetchdf()
        df.to_excel(writer, sheet_name=name, index=False)
