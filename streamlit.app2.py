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







