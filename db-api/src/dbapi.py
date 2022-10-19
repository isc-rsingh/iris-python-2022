# Embedded Python examples from summer 2022
import iris as dbapi
import time as time

mytable = "mypydbapi.test_things"
conn = dbapi.connect(hostname='localhost', port=1972, namespace='IRISAPP', username='_SYSTEM', password='SYS')

# Create table
cursor = conn.cursor()
try:
  cursor.execute(f"DROP TABLE {mytable}")
except Exception as inst:
  pass
try:
  cursor.execute(f"CREATE TABLE {mytable} (myvarchar VARCHAR(255), myint INTEGER, myfloat FLOAT)")
except Exception as inst:
  pass
cursor.close()
conn.commit()

# Create some data to fill in
numrows = 1000000
chunks = []
paramSequence = []
for row in range(numrows):
  paramSequence.append(["This is a non-selective string every row is the same data", row%10, row * 4.57292])
  if (row>0 and ((row % 10) == 0)):
    chunks.append(paramSequence)
    paramSequence = []
chunks.append(paramSequence)

query = f"INSERT INTO {mytable} (myvarchar, myint, myfloat) VALUES (?, ?, ?)"

start = time.time()
for chunk in chunks:
  cursor = conn.cursor()
  cursor.executemany(query, chunk)
  cursor.close()
  conn.commit()
# conn.close()
end = time.time()
elapsedtime = end - start
print("WRITE: elapsed time in seconds: " + str(elapsedtime))


sql = f"select * from {mytable}"
rowsRead = 0
cursor = conn.cursor()
cursor.arraysize = 20

start = time.time()
cursor.execute(sql)
rc = cursor.rowcount
rows = cursor.fetchall()
for row in rows:
  # print(row)
  x=0
rowsRead += len(rows)

end = time.time()
elapsedtime = end - start
print("READ: elapsed time in seconds: " + str(elapsedtime))

cursor.close()
conn.close()