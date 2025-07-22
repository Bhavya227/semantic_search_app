import streamlit as st
from data import sentences, sentence_embeddings, model
from search_engine import search

st.set_page_config(page_title="Semantic Search App", page_icon="🔍", layout="centered")

st.title("🔍 Simple Semantic Search Engine")
st.markdown("Enter a sentence below and we'll find the most semantically similar ones!")

user_query = st.text_input("💬 Your query:", "")

if user_query:
    query_embedding = model.encode(user_query, normalize_embeddings=True)
    results = search(query_embedding, sentence_embeddings, sentences)

    st.subheader("🔝 Top 3 Matches")
    for i, result in enumerate(results, 1):
        st.markdown(f"**{i}. {result['sentence']}**")
        st.progress(result["score"] / 100)
        st.caption(f"Similarity: {result['score']}%")
