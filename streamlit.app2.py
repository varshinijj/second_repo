import streamlit as st
import pandas as pd
import graphviz
st.set_page_config(layout="wide")

        
from graphviz import Digraph    
digraph cats {
  subgraph cluster_big_cats {
    // This subgraph is a cluster, because the name begins with "cluster"
    
    "Lion";
    "Snow Leopard";
  }

  subgraph domestic_cats {
    // This subgraph is also a cluster, because cluster=true.
    cluster=true;

    "Siamese";
    "Persian";
  }

  subgraph not_a_cluster {
    // This subgraph is not a cluster, because it doesn't start with "cluster",
    // nor sets cluster=true.
    
    "Wildcat";
  }
}






