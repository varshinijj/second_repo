import streamlit as st;
import pandas as pd;
import snowflake.connector;
conn = snowflake.connector.connect(
                user='VARSHINI',
                password='Snowflake@22!',
                account='bv18063.ap-southeast-1',
                ocsp_fail_open=False
                );
                
st.title("Snowflake Data-App") 

db = pd.read_sql("select database_name as database from SNOWFLAKE.ACCOUNT_USAGE.DATABASES where deleted is NULL and database_name not in ('SNOWFLAKE','SNOWFLAKE_SAMPLE_DATA');",conn)
dbs = list(set(list(db['DATABASE'])))
option = st.selectbox('select database:',dbs)
st.write('Selected Database :', option)
