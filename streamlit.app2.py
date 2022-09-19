import streamlit as st
import pandas as pd
import graphviz
st.set_page_config(layout="wide")
tabd = pd.DataFrame(columns=['db', 'sc', 'tab'])
tabd['db'] = ['db1','db1','db1','db1','db1','db1','db2','db2','db2','db2','db2','db2','db3','db3','db3','db3','db3','db3']
tabd['sc'] = ['db1s1','db1s1','db1s2','db1s2','db1s3','db1s3','db2s1','db2s1','db2s2','db2s2','db2s3','db2s3','db3s1','db3s1','db3s2','db3s2','db3s3','db3s3']
tabd['tab'] = ['tab111','tab112','tab121','tab122','tab131','tab132','tab211','tab212','tab221','tab222','tab231','tab232','tab311','tab312','tab321','tab322','tab331','tab332']

db = st.sidebar.selectbox("choose db:",tabd['db'])
sc = tabd.loc[tabd['db']==db][['sc','tab']]

col1, col2,col3 = st.columns([1, 4,5])


with col1:
    sel = ['All Schemas','Select Schemas']
    click = st.radio('Schemas:',sel)
    if click =='All Schemas':
        sc = tabd.loc[tabd['db']==db][['sc','tab']] 
    else:
        for x in list(sc['sc'].unique()): 
            schemas = st.checkbox('{}'.format(x),False,disabled=False)
            if schemas==False:
                sc = sc.loc[sc['sc']!=x]
        
    
    
    
 
with col2:
        
    d = graphviz.Digraph()
    d.attr(bgcolor='#0e1117')
    
    with d.subgraph() as s:
        s.attr(rank='same')
        s.node('{}'.format(db), fontcolor='white',color = 'red')  
    with d.subgraph() as s:
        s.attr(rank='same')
        for x in list(sc['sc'].unique()):
            s.node('{}'.format(x), fontcolor='white',color = 'red')
            d.edge('{}'.format(db),'{}'.format(x),color = 'white')
    with d.subgraph() as s:
        s.attr(rank='same')
        for idx,row in sc.iterrows():
            s.node('{}'.format(row['tab']), fontcolor='white',color = 'red')
            d.edge('{}'.format(row['sc']),'{}'.format(row['tab']),color = 'white')        
    st.graphviz_chart(d)
    
 with col3:
    
    c = graphviz.digraph {
        rankdir=LR;
        node [ shape=record ];
        struct1 [
            label = "a|b|<port1>c";
        ];
       }
    st.graphviz_chart(c)






