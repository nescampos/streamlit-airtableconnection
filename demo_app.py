import streamlit as st
from PIL import Image
from airtable_connection import AirtableConnection

image = Image.open('airtablelogo.png')
st.set_page_config(page_title="Airtable Connection")

st.image(image, caption='')



html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """

with st.sidebar:
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work
    Enter the access token, base id and table id from Airtable, then you can perform CRUD operations on your Airtable table.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    Made by [Néstor Campos](https://www.linkedin.com/in/nescampos/)
    """,
    unsafe_allow_html=True,
    )


st.markdown("## Airtable Connection")

st.markdown("""
### Connect to airtable and perform CRUD operations using Experimental Connections
""")

airtable_accesstoken = st.text("Enter your access token from Airtable API: ")
airtable_baseid = st.text("Enter your base id from Airtable API: ")
airtable_tablename = st.text("Enter your table name from Airtable API: ")

if st.button("Connect and get all records"):
    conn = st.experimental_connection("airtable",type=AirtableConnection,access_token=airtable_accesstoken)
    records = conn.get_all(airtable_baseid,airtable_tablename)

    st.write(records)

airtable_getrecordId = st.text("Enter your record id to search: ")

if st.button("Connect and get record"):
    conn = st.experimental_connection("airtable",type=AirtableConnection,access_token=airtable_accesstoken)
    record = conn.get(airtable_baseid,airtable_tablename,airtable_getrecordId)

    st.write(record)

airtable_createrecord = st.text("Enter your record to create (in Dictionary format): ", placeholder="{'Name': 'John'}")

if st.button("Connect and create record"):
    conn = st.experimental_connection("airtable",type=AirtableConnection,access_token=airtable_accesstoken)
    record = conn.create(airtable_baseid,airtable_tablename,airtable_createrecord)

    st.write(record)

airtable_updaterecordId = st.text("Enter your record id to update: ")
airtable_updatefields = st.text("Enter your record fields to update (in Dictionary format): ", placeholder="{'Age': 21}")

if st.button("Connect and update record"):
    conn = st.experimental_connection("airtable",type=AirtableConnection,access_token=airtable_accesstoken)
    record = conn.update(airtable_baseid,airtable_tablename,airtable_updaterecordId,airtable_updatefields)

    st.write(record)

airtable_deleterecordId = st.text("Enter your record id to delete: ")

if st.button("Connect and delete record"):
    conn = st.experimental_connection("airtable",type=AirtableConnection,access_token=airtable_accesstoken)
    record = conn.delete(airtable_baseid,airtable_tablename,airtable_deleterecordId)

    st.write(record)