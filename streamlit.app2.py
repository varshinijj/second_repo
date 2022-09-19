import streamlit as st
import pandas as pd
import graphviz
st.set_page_config(layout="wide")        
from graphviz import Digraph    

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')



  





