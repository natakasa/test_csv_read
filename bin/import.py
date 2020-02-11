import pandas as pd
import psycopg2
import sys
import os

app_home = os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)) , ".." ))
sys.path.append(os.path.join(app_home,"lib"))

print(sys.path)

from common import db
from common import test

df = pd.read_csv('./csv/test.csv')
print(df)

# insert実行
sql_str = "insert into t_csv_test (c1, c2, c3) values (%s, %s, %s)";

with db.get_connection() as conn:
    with conn.cursor() as cur:
        for row in df.itertuples():
            print(row.c1)
            cur.execute(sql_str, (row.c1, row.c2, row.c3))


