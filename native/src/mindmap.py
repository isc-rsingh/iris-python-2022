# Inspired by the "globals-mindmap" contest entry by Yuri Marx
# https://openexchange.intersystems.com/package/global-mindmap

import irisnative

# Write a JSON object to globals
def writeJSON(jo, irisnc):
    for key in jo:
        irisnc.set(jo[key], "^mymindmap", jo["id"], key)

# Make connection to InterSystems IRIS database
ip, port, namespace, username, pw = "localhost", 1972, "USER", "SuperUser", "SYS"
connection = irisnative.createConnection(ip, port, namespace, username, pw)
print("You have successfully connected to InterSystems IRIS.")

samplemap = {
    "id": "001", 
    "topic": "chicken", 
    "parent": "",
}
samplechild = {
    "id": "002", 
    "topic": "spicy wings", 
    "parent": "001",
}

# Create an InterSystems IRIS native object
irisnc = irisnative.createIris(connection)
st = writeJSON(samplemap, irisnc)
st = writeJSON(samplechild, irisnc)