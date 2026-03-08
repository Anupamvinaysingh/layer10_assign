import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


def show_graph(G):

    st.title("Memory Graph")

    fig = plt.figure()

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=2000
    )

    st.pyplot(fig)