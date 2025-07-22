# semantic_search_app


# 🔍 Semantic Search App with Dataset Upload, History & Charts

A Streamlit-powered Semantic Search app using Sentence Transformers. This version includes:
✅ Search history display
✅ Upload your own dataset (CSV/TXT)
✅ Bar chart visualization of similarity scores

Perfect for quickly exploring semantic similarity on custom datasets without any backend server setup.

📝 Features

* Pre-loaded default dataset (20+ sentences)
* Upload your own dataset via .csv or .txt
* Top 5 similar sentences displayed with similarity scores
* Cosine similarity using Sentence Transformers
* Search history tracking (resets on session end)
* Bar chart visualization of top results
* Responsive Streamlit UI

🚀 Quick Start Guide

1. Clone this repository
   git clone [https://github.com/yourusername/semantic-search-app.git](https://github.com/yourusername/semantic-search-app.git)
   cd semantic-search-app

2. Install dependencies
   pip install -r requirements.txt

3. Run the Streamlit app
   streamlit run app.py

The app will open in your browser at [http://localhost:8501](http://localhost:8501)

🖥️ Project Structure
semantic-search-app/
│
├── app.py                 → Streamlit UI logic
├── data.py                → Sentence dataset + embeddings
├── search\_engine.py       → Cosine similarity search logic
├── utils.py               → File upload handling
├── requirements.txt       → Python dependencies
└── README.md              → Project guide (this file)

💾 How to Use

* Enter your search query in the input box.
* View top similar sentences and their similarity percentages.
* See search history on the sidebar.
* Optional: Upload your own dataset (CSV/TXT) via sidebar to replace default sentences.
* View results as a bar chart under the results section.

🗂️ Dataset Upload Format

* .csv file → Single column of sentences (no header needed).
* .txt file → One sentence per line.

Example .txt:

This is a sample sentence.
Artificial Intelligence is changing the world.
SpaceX is exploring Mars.

Example .csv:

"This is a sample sentence."
"Artificial Intelligence is changing the world."
"SpaceX is exploring Mars."

📦 Dependencies

* streamlit
* sentence-transformers
* scikit-learn
* numpy
* pandas
* plotly

Install all using:
pip install -r requirements.txt

🧠 Model Used

* sentence-transformers/all-MiniLM-L6-v2 (small, fast, suitable for general semantic tasks).

🎉 Example Output:
Query: "Tell me something about AI"
Top Matches:

1. AI is changing the world rapidly. (92%)
2. Machine learning is a subset of AI. (87%)
3. Python is a popular programming language. (71%)

* Interactive bar chart of scores.

📌 Future Ideas (Optional Enhancements)

* Download search results as CSV
* Model selection dropdown
* Light/Dark mode toggle
* WordCloud visualization

👨‍💻 Author
Made by Bhavya Shah

📃 License
MIT License — Free to use, modify, and distribute.


