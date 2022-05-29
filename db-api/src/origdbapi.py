import sys
import contextlib
import time
import iris as dbapi

mytable = "mypydbapi.test_things"

class Test():
  def connect(self):
    return dbapi.connect(hostname='localhost', port=1972, namespace='IRISAPP', username='_SYSTEM', password='SYS')

  def CreateTable(self):
    conn = self.connect()
    cursor = conn.cursor()
    try:
        cursor.execute(f"CREATE TABLE {mytable} (myvarchar VARCHAR(255), myint INTEGER, myfloat FLOAT)")
    except Exception as inst:
      pass
    cursor.close()
    conn.commit()

  def PopulateTable(self, numRows, chunkSize):
    conn = self.connect()

    # Create some data to fill in
    chunks = []
    paramSequence = []
    for row in range(numRows):
      paramSequence.append(["This is a non-selective string every row is the same data", row%10, row * 4.57292])
      if (row>0 and ((row % chunkSize) == 0)):
        chunks.append(paramSequence)
        paramSequence = []
    chunks.append(paramSequence)

    query = f"INSERT INTO {mytable} (myvarchar, myint, myfloat) VALUES (?, ?, ?)"

    for chunk in chunks:
      cursor = conn.cursor()
      cursor.executemany(query, chunk)
      cursor.close()
      conn.commit()
    conn.close()

  def QueryTable(self, readChunkSize, sql):
    conn = self.connect()

    rowsRead = 0
    cursor = conn.cursor()
    if readChunkSize:
      cursor.arraysize = readChunkSize
    cursor.execute(sql)
    rc = cursor.rowcount
    rows = cursor.fetchall()
    for row in rows:
      print(row)
    rowsRead += len(rows)

    cursor.close()
    conn.close()

  def Test(self):
    print("creating table")
    self.CreateTable()
    print("populating table")
    self.PopulateTable(100, 10)
    print("queryinging table")
    self.QueryTable(20, f"select * from {mytable}")


t = Test()
t.Test()
