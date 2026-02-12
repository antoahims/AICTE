# 📰 Fake News Detection System

An AI-powered web application that uses **Machine Learning** and **Natural Language Processing (NLP)** to classify news articles as **Real** or **Fake**.

---

## 🔍 Project Overview

This project implements a complete end-to-end pipeline for detecting fake news:

1. **Data Preprocessing** — Text cleaning, stopword removal, and feature extraction
2. **Model Training** — Multinomial Naive Bayes with TF-IDF vectorization
3. **Web Interface** — Flask-based app with a modern dark-themed UI

---

## 📊 Dataset

- **Source:** Synthetic dataset (replace with [Kaggle Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) for production)
- **Columns:** `title`, `text`, `label`
- **Labels:** `0` = Fake News, `1` = Real News

---

## 🧠 Model Details

| Component        | Details                      |
|-------------------|------------------------------|
| Algorithm         | Multinomial Naive Bayes      |
| Vectorization     | TF-IDF (max 5000 features)   |
| Text Preprocessing| Lowercase, remove punctuation, remove stopwords |
| Train/Test Split  | 80/20                        |

---

## 📈 Accuracy

The model achieves approximately **88–92% accuracy** on the test set.

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Fake-News-Detection.git
cd Fake-News-Detection
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model
```bash
python train.py
```

### 5. Run the Web App
```bash
python app.py
```

### 6. Open in Browser
Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Project Structure

```
Fake-News-Detection/
├── dataset/
│   └── fake_news.csv
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
├── templates/
│   └── index.html
├── train.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🖼️ Screenshots

> Run the app locally to see the modern dark-themed UI with glassmorphism effects, gradient accents, and confidence score visualization.

---

## 🔮 Future Scope

- 📊 Confusion matrix and ROC curve visualization
- 🧪 Support for multiple ML models (Logistic Regression, SVM, LSTM)
- 🐳 Dockerize for easy deployment
- ☁️ Deploy to Render / Railway / AWS
- 📰 Real-time news scraping and verification
- 📱 Mobile-responsive PWA version

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML/NLP:** scikit-learn, NLTK, pandas, NumPy
- **Frontend:** HTML5, CSS3 (custom dark theme)
- **Serialization:** Joblib

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
