# Embedded Python examples from summer 2022
import iris
import time as time

mytable = "mypydbapi.test_things"

# Create table
try:
  iris.sql.exec(f"DROP TABLE {mytable}")
except Exception as inst:
  pass
try:
  iris.sql.exec(f"CREATE TABLE {mytable} (myvarchar VARCHAR(255), myint INTEGER, myfloat FLOAT)")
except Exception as inst:
  pass

# Create some data to fill in
numrows = 1000000
paramSequence = []
for row in range(numrows):
  paramSequence.append(["This is a non-selective string every row is the same data", row%10, row * 4.57292])

stmt = iris.sql.prepare(f"INSERT INTO {mytable} (myvarchar, myint, myfloat) VALUES (?, ?, ?)")
start = time.time()
for r in paramSequence:
  stmt.execute(r[0], r[1], r[2])
end = time.time()
elapsedtime = end - start
print("WRITE: elapsed time in seconds: " + str(elapsedtime))

start = time.time()
df = iris.sql.exec(f"SELECT * FROM {mytable}").dataframe()
end = time.time()
elapsedtime = end - start
print("READ: elapsed time in seconds: " + str(elapsedtime))

print(df.head())
print(df.describe())
