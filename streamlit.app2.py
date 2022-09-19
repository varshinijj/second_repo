import streamlit as st
import pandas as pd
import graphviz
st.set_page_config(layout="wide")

        
from graphviz import Digraph    

Digraph {
  graph[bgcolor = "#FDFDFD"]
  graph [newrank=true] // added
  node[fontname = "helvetica-bold", width = 1.5, height = 0.5, fontsize=12]
  rankdir=TB;

    subgraph cluster_main {
    style=dashed; color= "#625a5a"; 
    label="Steps for \n Scientometric Analysis"
    graph[rankdir=TB]
    node [shape=box, style=filled, color=black, fillcolor = "#91cf60"];
    node [group=vert]  // added
      a[label = "Section 1 \n Descriptive Analysis"]
      b[label = "Section 2 \n Intellectual Structure"]
      c[label = "Section 3 \n Historiograph"]
      d[label = "Section 4 \n Conceptual structure"]
      e[label = "Section 5 \n Thematic Map"]
      f[label = "Section 6 \n Social structure"]
      a -> b -> c -> d -> e -> f}

    subgraph cluster_a {
    color= "#625a5a";
    node [shape=box, style = filled, color=black, fillcolor = "#fee08b"];
      a4[label = "Top manuscripts"]
      a3[label = "Most Productive \n Authors"]
      a2[label = "Most Cited \n References"]
      a1[label = "Main findings"]}  
    
    subgraph cluster_b {
    color= "#625a5a";
    node [shape=box, style = filled, color=black, fillcolor = "#fee08b"];
      b4[label = "Source \n coupling analysis"]
      b3[label = "Source \n co-citation analysis"]
      b2[label = "Article \n coupling analysis"]
      b1[label = "Article \n co-citation analysis"]}

    subgraph cluster_d {
    color= "#625a5a";
    node [shape=box, style = filled, color=black, fillcolor = "#fee08b"];
     d4[label = "Title & Abstract \n Term Analysis"]
     d3[label = "Correspondence Analysis \n for both Keywords"]
     d2[label = "Author Keyword \n Co-occurrence & Growth"]
     d1[label = "Keyword-Plus \n Co-occurrence & Growth"]}

    subgraph cluster_f {
    color= "#625a5a";
    node [shape=box, style = filled, color=black, fillcolor = "#fee08b"];
        f4[label = "Country \n Collaboration Network"]
        f3[label = "Edu \n Collaboration Network"]
        f2[label = "Author \n Collaboration Network"]
        f1[label = "Three Fields \n Plots"]
    }

    // added rank=same
    {rank = same a -> {a1 a2 a3 a4} }
    {rank = same b -> {b1 b2 b3 b4} }
    {rank = same d -> {d1 d2 d3 d4} }
    {rank = same f -> {f1 f2 f3 f4} }

    edge[style=invis]
      a1 -> b1 -> d1 -> f1
      a2 -> b2 -> d2 -> f2
      a3 -> b3 -> d3 -> f3
      a4 -> b4 -> d4 -> f4
 }
  





