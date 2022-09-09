import streamlit as st
import pandas as pd
import graphviz


d = graphviz.Digraph()

with d.subgraph() as s:
    s.attr(rank='same')
    s.node('A')
    s.node('X')

d.node('C')

with d.subgraph() as s:
    s.attr(rank='same')
    s.node('B')
    s.node('D')
    s.node('Y')

d.edges(['AB', 'AC', 'CD', 'XY'])

st.graphviz_chart(d)
salgrade = pd.DataFrame(columns=['GRADE', 'LOSAL', 'HISAL'])
salgrade['GRADE'] = [1,2,3,4,5]
salgrade['LOSAL'] = [700,1201,1401,2001,3001]
salgrade['HISAL'] = [1200,1400,2000,3000,9999]
salgrade







