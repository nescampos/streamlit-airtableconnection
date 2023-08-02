# streamlit-airtableconnection

Now you can connect to [Airtable](https://airtable.com/) using [Streamlit Connection](https://docs.streamlit.io/library/advanced-features/connecting-to-data).

Demo: https://airtableexperimentalconnection.streamlit.app/

## How works

Just get an access token from Airtable and use the connection in Streamlit.

```python 
from airtable_connection import AirtableConnection

conn = st.experimental_connection("airtable",type=AirtableConnection,access_token=airtable_accesstoken)
```

## What can you do? 

**get_all**: Get all information from a table. 

```python 
records = conn.get_all(airtable_baseid,airtable_tablename,ttl_for_cache)
st.write(records)
```

**get**: Get a record from the table. 

```python 
record = conn.get(airtable_baseid,airtable_tablename,airtable_getrecordId,ttl_for_cache)
st.write(record)
```

**create**: Create a new record on the table. _The record data needs to be in a Dict/JSON format.

```python 
record = conn.create(airtable_baseid,airtable_tablename,airtable_createrecord)
st.write(record)
```

**update**: Update a record on the table. _The field data need to be in a Dict/JSON format.

```python 
record = conn.update(airtable_baseid,airtable_tablename,airtable_updaterecordId,airtable_updatefields)
st.write(record)
```

**delete**: Delete a record on the table.

```python 
record = conn.delete(airtable_baseid,airtable_tablename,airtable_deleterecordId)
st.write(record)
```
