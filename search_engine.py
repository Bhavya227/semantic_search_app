from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def search(query_embedding, sentence_embeddings, sentences, top_k=3):
    similarities = cosine_similarity([query_embedding], sentence_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    
    results = []
    for idx in top_indices:
        score = similarities[idx]
        results.append({
            "sentence": sentences[idx],
            "score": round(float(score) * 100, 2)  # Convert to percentage
        })
    return results
