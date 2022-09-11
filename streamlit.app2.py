import streamlit as st
import pandas as pd
import graphviz

tabd = pd.DataFrame(columns=['db', 'sc', 'tab'])
tabd['db'] = ['db1','db1','db1','db1','db1','db1','db2','db2','db2','db2','db2','db2','db3','db3','db3','db3','db3','db3']
tabd['sc'] = ['db1s1','db1s1','db1s2','db1s2','db1s3','db1s3','db2s1','db2s1','db2s2','db2s2','db2s3','db2s3','db3s1','db3s1','db3s2','db3s2','db3s3','db3s3']
tabd['tab'] = ['tab111','tab112','tab121','tab122','tab131','tab132','tab211','tab212','tab221','tab222','tab231','tab232','tab311','tab312','tab321','tab322','tab331','tab332']
base="light"
db = st.sidebar.selectbox("choose db:",tabd['db'])
sc = tabd.loc[tabd['db']==db][['sc','tab']]

col1, col2 = st.columns([1, 4])

with col1:
    allschemas = st.checkbox('All schemas',True)
    for x in list(sc['sc'].unique()):
        schemas = st.checkbox('{}'.format(x),False)
        if schemas==False:
            sc =sc.loc[sc['sc']!=x]
        if schemas==True:
            sc = sc.loc[sc['sc']==x]
            allschemas = False
    if allschemas:
        sc = tabd.loc[tabd['db']==db][['sc','tab']] 
 
        
        
            

        
        
with col2:
    d = graphviz.Digraph()
    d.attr(bgcolor='grey', fontcolor='white')
    
    with d.subgraph() as s:
        s.attr(rank='same')
        s.node('{}'.format(db))  
    with d.subgraph() as s:
        s.attr(rank='same')
        for x in list(sc['sc'].unique()):
            s.node('{}'.format(x))
            d.edge('{}'.format(db),'{}'.format(x),label='m', len='1.00')
    with d.subgraph() as s:
        s.attr(rank='same')
        for idx,row in sc.iterrows():
            s.node('{}'.format(row['tab']))
            d.edge('{}'.format(row['sc']),'{}'.format(row['tab']))        
    st.graphviz_chart(d)
    





