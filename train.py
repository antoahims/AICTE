import pandas as pd
import nltk
import string
import joblib
import os

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

nltk.download('stopwords')

# Load Kaggle dataset (Fake.csv + True.csv)
df_fake = pd.read_csv("dataset/Fake.csv")
df_fake["label"] = 0

df_true = pd.read_csv("dataset/True.csv")
df_true["label"] = 1

df = pd.concat([df_fake, df_true], ignore_index=True)
print(f"Loaded {len(df_fake)} fake + {len(df_true)} real = {len(df)} total")

# Combine title and text
df["content"] = df["title"] + " " + df["text"]

# Drop null values
df = df.dropna()

# Text cleaning function
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

df["content"] = df["content"].apply(clean_text)

# Features and labels
X = df["content"]
y = df["label"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(X)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model and vectorizer
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model training complete and saved.")
