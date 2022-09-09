import streamlit as st
import pandas as pd
import graphviz

tabd = pd.DataFrame(columns=['db', 'sc', 'tab'])
tabd['db'] = ['db1','db1','db1','db1','db1','db1','db2','db2','db2','db2','db2','db2','db3','db3','db3','db3','db3','db3']
tabd['sc'] = ['db1s1','db1s1','db1s2','db1s2','db1s3','db1s3','db2s1','db2s1','db2s2','db2s2','db2s3','db2s3','db3s1','db3s1','db3s2','db3s2','db3s3','db3s3']
tabd['tab'] = ['tab111','tab112','tab121','tab122','tab131','tab132','tab211','tab212','tab221','tab222','tab231','tab232','tab311','tab312','tab321','tab322','tab331','tab332']
tabd

db = st.sidebar.selectbox("choose db:",tabd['db'])
d = graphviz.Digraph()

with d.subgraph() as s:
    s.attr(rank='same')
    s.node('A')
    s.node('{}'.format(db))   

d.node('C')

with d.subgraph() as s:
    s.attr(rank='same')
    s.node('B')
    s.node('D')
   

d.edges(['AB', 'AC', 'CD'])

st.graphviz_chart(d)





