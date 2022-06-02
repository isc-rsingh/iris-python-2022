/// Embedded Python examples from summer 2022
Class Sample.EmbeddedPython Extends %RegisteredObject
{

ClassMethod dfexample() As %Status
{
    set st = ..CreateDataFrame("Name, Super, TimeCreated")
}

// Execute a SQL query from Python and import it into a pandas dataframe

ClassMethod CreateDataFrame(myfields As %String) As %Numeric [ Language = python ]
{
    import iris
    import pandas as pd
    #; works with all IRIS installs
    rs = iris.sql.exec("SELECT " + myfields + " FROM %Dictionary.ClassDefinition WHERE Name %STARTSWITH '%Net.'")
    #; works with Titanic sample data
    #; rs = iris.sql.exec("SELECT " + fields + " FROM Data.Titanic")
    df = rs.dataframe()
    print(df.describe())
    return True
}

/// Description
ClassMethod GetDatasetProperties(dataset As %String) As %Status
{
    try {
    set sqlquery = "SELECT TOP 1 * FROM "_dataset
    set rs = ##class(%SQL.Statement).%ExecDirect(,sqlquery)
    set cols = rs.%GetMetadata().columns
    set idx = 1
    set props = ""
    write "{""properties"":[" 
    while idx<=rs.%ResultColumnCount {
        set props = props_"{"""_cols.GetAt(idx).colName_""": "
        set props = props_cols.GetAt(idx).clientType_"},"
        set idx = idx + 1
    }
    write $EXTRACT(props,1,*-1)
    write "]}"
    } catch (oException) {
    write oException
    }
    Return $$$OK
}

}
