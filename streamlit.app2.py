import streamlit as st
import pandas as pd
import graphviz
st.set_page_config(layout="wide")        
from graphviz import Digraph    

st.graphviz_chart('''
    digraph ok {
  subgraph cluster_0{
     { rank=same  // all nodes on same rank
       node [shape ="rectangle"]    // for all nodes in this subgraph
       edge [style=invis]           // for all edges, invisible links
       // we use the invisible edges to establish their sequence (kludge)
       name0 ->  name1 ->  name2 
     }
  }
}
''')



  





