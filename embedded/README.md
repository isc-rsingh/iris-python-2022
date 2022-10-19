# InterSystems IRIS with Embedded Python

This program demonstrates using Python _running in the database_ and SQL with IRIS as a data layer. 
It measures the performance of simple reads and writes to the database.

## Setup

1. start the container: `docker-compose up`
2. open a bash shell on the container
3. run `cd /irisdev/app/src`
4. run `irispython explore.py`

## Results

### with 100,000 numrows
WRITE: elapsed time in seconds: 1.6012108325958252
READ: elapsed time in seconds: 0.959336519241333

### with 1,000,000 numrows
WRITE: elapsed time in seconds: 15.509956359863281
READ: elapsed time in seconds: 2.699157476425171
