from sentence_transformers import SentenceTransformer
import numpy as np

# Dataset of sentences
sentences = [
    "The sun sets over the mountains.",
    "A cat sleeps on the warm windowsill.",
    "SpaceX launched another rocket into orbit.",
    "Machine learning is a subset of AI.",
    "He plays the guitar beautifully.",
    "The car broke down on the highway.",
    "Python is a popular programming language.",
    "Rainy days make me feel calm.",
    "She baked a chocolate cake.",
    "The library is quiet and peaceful.",
    "Electric cars are the future of transportation.",
    "Birds chirp loudly in the morning.",
    "The movie had an unexpected ending.",
    "He studies quantum physics.",
    "They went hiking in the forest.",
    "The concert was a blast!",
    "Reading books expands your mind.",
    "Dogs are loyal companions.",
    "He solved the puzzle quickly.",
    "The coffee shop was crowded today.",
    "AI is changing the world rapidly.",
    "She paints abstract landscapes.",
    "Mount Everest is the tallest mountain.",
    "Data science combines stats and programming.",
    "The storm caused a power outage."
]

# Load pre-trained model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate and cache embeddings
sentence_embeddings = model.encode(sentences, normalize_embeddings=True)
