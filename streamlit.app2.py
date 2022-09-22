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

st.sidebar.title("Choose Database to Classify")
DB = st.sidebar.radio('Available Databases:',all_databases())
  
  
##export
def convert_df(df):
  return df.to_csv().encode('utf-8')

##final

def schemas_tables():
  
  sc = pd.read_sql("select CATALOG_NAME AS DATABASE,SCHEMA_NAME AS SCHEMA from {}.information_schema.SCHEMATA where SCHEMA_NAME !='INFORMATION_SCHEMA';".format(DB),conn)
  sc_tb = pd.read_sql("select TABLE_CATALOG as database,TABLE_SCHEMA AS SCHEMA,TABLE_NAME from {}.information_schema.TABLES where TABLE_SCHEMA != 'INFORMATION_SCHEMA';".format(DB),conn)
  
  tab1, tab2 = st.tabs(["Detailed view",  "overview"])
  with tab1:
    col1, col2 = st.columns([8,2])
    with col1:
      select = ['Select Schemas','All Schemas']
      click = st.radio('SCHEMAS',select,key=2,horizontal=True)
  
      if click =='All Schemas':
        pass 
      else:
        schemas = st.multiselect('',list(sc['SCHEMA']),key=1)
        schema= (str(schemas)[1:-1])
        schema #testing purpose
        for n in list(sc['SCHEMA']):
          if n not in schema:
            sc = sc.loc[sc['SCHEMA']!=n]
            sc_tb = sc_tb.loc[sc_tb['SCHEMA']!=n]
            
      click2 = st.radio('TABLES',['Select Tables','All Tables'],key=3,horizontal=True) 
      if click2 =='All Tables':
        pass
      else:
        tables = st.multiselect('',list(sc_tb['TABLE_NAME']),key=4)
        tables = (str(tables)[1:-1])
        tables #testing purpose
        for n in list(sc_tb['TABLE_NAME']):
          if n not in tables:
            sc_tb = sc_tb.loc[sc_tb['TABLE_NAME']!=n]
  return sc_tb          
            
if st.sidebar.button("Apply",key=7):
  st.experimental_memo.clear()           
            
def classify():     
   
   sc_tb = schemas_tables()   
   if st.button("Classify"):   
     if sc_tb.shape[0]!=0:
       alltags = pd.DataFrame(columns=['SCHEMA', 'TABLE_NAME', 'COLUMN_NAME','TAG_NAME','TAG_VALUE'])
       alldatatypes = pd.DataFrame(columns=['DATABASE','SCHEMA', 'TABLE_NAME', 'COLUMN_NAME','DATA_TYPE'])
       for idx,row in sc_tb.iterrows():
         conn.cursor().execute("call ASSOCIATE_SEMANTIC_CATEGORY_TAGS('{}.{}.{}',EXTRACT_SEMANTIC_CATEGORIES('{}.{}.{}'));".format(DB,row['SCHEMA'],row['TABLE_NAME'],DB,row['SCHEMA'],row['TABLE_NAME']))        
         tags = pd.read_sql("select OBJECT_SCHEMA as schema,OBJECT_NAME as table_name,COLUMN_NAME,TAG_NAME,TAG_VALUE from table({}.information_schema.tag_references_all_columns('{}.{}.{}','table'));".format(DB,DB,row['SCHEMA'],row['TABLE_NAME']),conn)         
         datatype = pd.read_sql("select TABLE_CATALOG as database,TABLE_SCHEMA as schema,TABLE_NAME,COLUMN_NAME ,DATA_TYPE  FROM {}.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA ='{}' and TABLE_NAME = '{}';".format(DB,row['SCHEMA'],row['TABLE_NAME']),conn)
         alltags = alltags.append(tags, ignore_index=True) 
         alldatatypes = alldatatypes.append(datatype,ignore_index=True)
       if alltags.shape[0]!=0:  
         tags_pivot = alltags.pivot(index=['SCHEMA','TABLE_NAME','COLUMN_NAME'],columns=['TAG_NAME'],values=['TAG_VALUE']).reset_index()
         tags_tb = tags_pivot[['SCHEMA','TABLE_NAME']]
         tags_tb_grouped = tags_tb.groupby(['SCHEMA','TABLE_NAME']).size().reset_index(name='no.of.sensitive_col')
         alldatatypes = alldatatypes.rename(columns = {'TABLE_NAME':'TABLE NAME','ÇOLUMN_NAME':'COLUMN NAME','DATA_TYPE':'DATA TYPE'})
         display=pd.merge(sc_tb,tags_pivot, on=['SCHEMA'], how='inner').rename(columns={('TABLE_NAME',''):'TABLE NAME',('COLUMN_NAME',''):'COLUMN NAME',('TAG_VALUE','SEMANTIC_CATEGORY'):'SEMANTIC CATEGORY',('TAG_VALUE','PRIVACY_CATEGORY'):'PRIVACY CATEGORY'})
         final = pd.merge(display,alldatatypes,left_on=['DATABASE','SCHEMA','TABLE NAME','COLUMN NAME'],right_on=['DATABASE','SCHEMA','TABLE NAME','COLUMN_NAME'], how = 'left').drop(['COLUMN_NAME'],axis=1)
         final = final[['DATABASE','SCHEMA','TABLE NAME','COLUMN NAME','DATA TYPE','PRIVACY CATEGORY','SEMANTIC CATEGORY']]
         final
         csv = convert_df(final)
         st.download_button("Export Report",data=csv,file_name='Tags.csv',mime='text/csv')
       else:
         st.info('No columns in any of the tables has any sensitive data', icon="ℹ️")
     elif sc.shape[0]!=0:
       st.info('No Tables under the schema', icon="ℹ️")
     else:
       st.error('Please select a schema', icon="🚨")         


table = classify()


    









