# InterSystems IRIS with Python DB-API

This program demonstrates using Python and SQL _through a DBAPI driver_ with IRIS as a data layer. 
It measures the performance of simple reads and writes to the database.

## Setup

1. start the container: `docker-compose up`
2. open a bash shell on the container
3. run `cd /irisdev/app/src`
4. run `python3 dbapi.py`

## Results

### with 100,000 numrows
WRITE: elapsed time in seconds: 3.9308974742889404
READ: elapsed time in seconds: 1.5049290657043457

### with 1,000,000 numrows
WRITE: elapsed time in seconds: 39.856650829315186
READ: elapsed time in seconds: 10.62797498703003
