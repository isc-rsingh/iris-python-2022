# Embedded Python examples from summer 2022
import iris as dbapi

mytable = "mypydbapi.test_things"
conn = dbapi.connect(hostname='localhost', port=1972, namespace='IRISAPP', username='_SYSTEM', password='SYS')

# Create table
cursor = conn.cursor()
try:
  cursor.execute(f"CREATE TABLE {mytable} (myvarchar VARCHAR(255), myint INTEGER, myfloat FLOAT)")
except Exception as inst:
  pass
cursor.close()
conn.commit()

# Create some data to fill in
chunks = []
paramSequence = []
for row in range(10):
  paramSequence.append(["This is a non-selective string every row is the same data", row%10, row * 4.57292])
  if (row>0 and ((row % 10) == 0)):
    chunks.append(paramSequence)
    paramSequence = []
chunks.append(paramSequence)

query = f"INSERT INTO {mytable} (myvarchar, myint, myfloat) VALUES (?, ?, ?)"

for chunk in chunks:
  cursor = conn.cursor()
  cursor.executemany(query, chunk)
  cursor.close()
  conn.commit()
# conn.close()

sql = f"select * from {mytable}"
rowsRead = 0
cursor = conn.cursor()
cursor.arraysize = 20

cursor.execute(sql)
rc = cursor.rowcount
rows = cursor.fetchall()
for row in rows:
  print(row)
rowsRead += len(rows)

cursor.close()
conn.close()