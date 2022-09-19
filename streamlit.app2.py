import streamlit as st
import pandas as pd
import graphviz
st.set_page_config(layout="wide")

        
from graphviz import Digraph    
    
    
 


g = Digraph(node_attr={'shape':'box', 'style': 'rounded,filled'})

# NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
#       so that Graphviz recognizes it as a special cluster subgraph

with g.subgraph(name='cluster_A',) as c:
    c.attr(shape='box', style= 'rounded,filled', color='#82d2f0', label='Cluster A')
    c.attr('node', color='blue',)
    c.node('Node A')
    c.node('Node B')
    
with g.subgraph(name='cluster_B') as a:
    a.attr(shape='box', style= 'rounded,filled', color='#fac800', label='Cluster B')
    a.attr('node', color='orange')
    a.node('Node C')
    a.node('Node D')
    
    with a.subgraph(name='cluster_B_1') as b:
        b.attr(shape='box', style= 'rounded,filled', color='yellow', label='Cluster B 1')
        b.node('Node E')
        b.node('Node F')



g.edge('cluster_B_1', 'Node A')
g.render('GraphvizTest', cleanup=True)






