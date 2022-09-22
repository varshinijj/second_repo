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


def all_databases():
  db_data = pd.read_sql("select database_name as database from SNOWFLAKE.ACCOUNT_USAGE.DATABASES where database_name not in ('SNOWFLAKE','SNOWFLAKE_SAMPLE_DATA') and deleted is null;",conn)
  dbs = list(set(list(db_data['DATABASE'])))
  return dbs


def schema_sc():
  st.sidebar.title("Choose Database to Classify")
  DB = st.sidebar.radio('Available Databases:',all_databases())
  sc = pd.read_sql("select CATALOG_NAME AS DATABASE,SCHEMA_NAME AS SCHEMA from {}.information_schema.SCHEMATA where SCHEMA_NAME !='INFORMATION_SCHEMA';".format(DB),conn)
  return sc

sc = schema_sc()
  





