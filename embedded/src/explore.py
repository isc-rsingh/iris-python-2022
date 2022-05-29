import json
import pandas
import iris

# GET properties from a given dataset
def GetDatasetProperties(dataset: str):
    sqlquery = "SELECT TOP 1 * FROM " + dataset
    try:
        rs = iris.sql.exec(sqlquery)
        cols = rs.ResultSet._GetMetadata().columns
        idx = 1
        props = {}
        props["properties"] = list()
        while idx <= len(cols):
            propName= cols.GetAt(idx).colName
            propType= cols.GetAt(idx).clientType
            idx=idx+1
            props["properties"].append({propName:propType})

        return props
    except Exception as e:
        raise e

# Get info for a prop
def Explore(dataset,prop,type):
    if int(type) == 16: 
        rs = iris.sql.exec('SELECT "' + prop + '" as val, count("'+prop+'") as cnt FROM ' + dataset + ' GROUP BY "' + prop + '"')
        ret = {}
        tfcounts = [] 
        cnt = 0
        for idx, row in enumerate(rs):
            tfcounts.insert(0, {"value": row[0], "count": row[1]})
            cnt += row[1]
        ret["tfcounts"] = tfcounts
        ret["count"] = cnt
        return json.dumps(ret)
 
    # if we're here we know it's not a boolean
    rs = iris.sql.exec('SELECT "' + prop + '" FROM ' + dataset)
    df = rs.dataframe()
    b = df[prop.lower()].describe()
 
    # no data case
    if (b["count"] == 0):
        ret = { "count": 0 }

    ret = json.loads(b.to_json())
    # @TODO handle strings better
    if type == 10:
        return json.dumps(ret)

    # this is good for numeric values
    elif ("min" in b):
        c = df[prop.lower()].value_counts(bins=10, sort=False)
        clist = []
        for iv in c.iteritems(): 
            d = {}
            ivlr = str(iv[0].left) + " - " + str(iv[0].right)
            d['value'] = iv[1]
            d['left'] = str(iv[0].left)
            d['right'] = str(iv[0].right)
            clist.append(d)
        ret["bins"] = clist
        return json.dumps(ret)
    
    return json.dumps(ret)
    
# Print out a list of properties and their IRIS data type code
# For property type codes see: https://docs.intersystems.com/irislatest/csp/documatic/%25CSP.Documatic.cls?&LIBRARY=%25SYS&CLASSNAME=%25SQL.StatementColumn#PROPERTY_clientType
dataset = "Data.Titanic"
response = GetDatasetProperties(dataset)
pretty = json.dumps(response, indent=2)
print(f"\nProperties for: {dataset}:")
print(pretty)

# Print descriptive statistics for a property
prop = "Survived"
response = Explore(dataset, prop, 5)
print(f"\nStats for: {prop}:")
print(response)
