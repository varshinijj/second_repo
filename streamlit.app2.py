import streamlit as st
import plotly.graph_objects as go
import graphviz as graphviz
import pandas as pd
import snowflake.connector
st.set_page_config(layout="wide")

####connecting to snowflake account####

conn = snowflake.connector.connect(
                user='VARSHINI',
                password='Snowflake@22!',
                account='bg35464.ap-southeast-1',
                warehouse = 'SQLWH',
                ocsp_fail_open=False)

cur = conn.cursor() 

####database selection####

##DB
@st.experimental_singleton
def all_databases():
  db_data = pd.read_sql("select database_name as database from SNOWFLAKE.ACCOUNT_USAGE.DATABASES where database_name not in ('SNOWFLAKE','SNOWFLAKE_SAMPLE_DATA') and deleted is null;",conn)
  dbs = list(set(db_data['DATABASE']))
  return dbs

##export
def convert_df(df):
  return df.to_csv().encode('utf-8')

##final
def all_data():
  st.sidebar.title("Choose Database to Classify")
  DB = st.sidebar.radio('Available Databases:',all_databases())
  sc = pd.read_sql("select CATALOG_NAME AS DATABASE,SCHEMA_NAME AS SCHEMA from {}.information_schema.SCHEMATA where SCHEMA_NAME !='INFORMATION_SCHEMA';".format(DB),conn)
  sc_tb = pd.read_sql("select TABLE_SCHEMA AS SCHEMA,TABLE_NAME from {}.information_schema.TABLES where TABLE_SCHEMA != 'INFORMATION_SCHEMA';".format(DB),conn)
  
  tab1, tab2 = st.tabs(["Detailed view",  "overview"])
  with tab1:
    col1, col2 = st.columns([8,2])
    with col1:
      select = ['All Schemas','Select Schemas']
      click = st.radio('Choose Schema:',select,key=2,horizontal=True)
  
      if click =='All Schemas':
        pass
      else:
        for x in list(sc['SCHEMA']):
          schemas = st.checkbox('{}'.format(x),False)
          if schemas==False:
            sc = sc.loc[sc['SCHEMA']!=x]
            sc_tb = sc_tb.loc[sc_tb['SCHEMA']!=x] 
  return sc           


table = all_data()







