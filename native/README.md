# InterSystems IRIS with Python Native API

1. start the container: `docker-compose up`
2. open a terminal on the container
3. run `cd /opt/irisbuild/src`
4. run `python3 mindmap.py`

Then view the data you have written to the database

1. from the terminal, run `iris session IRIS`
2. run `write ^mymindmap("001","topic")`
3. run `halt`