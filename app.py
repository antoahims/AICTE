from flask import Flask, render_template, request
import joblib
import string
from nltk.corpus import stopwords
import nltk
import numpy as np

nltk.download('stopwords')

app = Flask(__name__)

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None
    news_text = ""

    if request.method == "POST":
        news = request.form["news"]
        news_text = news
        cleaned = clean_text(news)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        probabilities = model.predict_proba(vectorized)[0]
        confidence = round(max(probabilities) * 100, 1)

        result = "Real News ✅" if prediction == 1 else "Fake News ❌"

        return render_template("index.html", result=result, confidence=confidence, news_text=news_text)

    return render_template("index.html", result=result, confidence=confidence, news_text=news_text)

if __name__ == "__main__":
    app.run(debug=True)
