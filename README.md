# 🛡️ Real-Time Fraud Detection System

> End-to-end Machine Learning pipeline for detecting fraudulent financial transactions using **LightGBM**, **SHAP Explainable AI**, and an interactive **Streamlit Dashboard**.
---

## 📌 Overview

This project builds a complete fraud detection system on the **IEEE-CIS Fraud Detection** dataset. It handles the challenge of severely imbalanced data using SMOTE, trains a high-performance LightGBM model, explains every prediction using SHAP, and exposes all of this through an interactive Streamlit dashboard.

Suitable for: **Resume Projects · Internship Applications · Academic Submissions · Portfolio Showcase**

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚡ **LightGBM Classifier** | Fast, high-accuracy fraud detection on tabular data |
| 🧠 **SHAP Explainability** | Per-prediction feature importance and summary plots |
| 📊 **Streamlit Dashboard** | Live fraud prediction, analytics, and risk segmentation |
| ⚖️ **SMOTE Balancing** | Handles severe class imbalance between fraud and non-fraud |
| 🛠️ **Feature Engineering** | Domain-specific fraud signals derived from transaction patterns |
| 🔍 **Risk Segmentation** | Transaction explorer with real-time risk scoring |
| 📈 **Full Evaluation Suite** | Accuracy, F1, ROC-AUC, Confusion Matrix |

---

## 🧰 Tech Stack

```
Python · Pandas · NumPy · Scikit-learn · LightGBM · SHAP
Imbalanced-learn · Matplotlib · Seaborn · Plotly · Streamlit
```

---

## 📂 Project Structure

```
FraudDetection_Ayush/
│
├── analysis.ipynb              ← Main ML notebook (EDA → Training → SHAP)
├── requirements.txt
├── README.md
│
├── data/
│   ├── train_transaction.csv   ← IEEE-CIS transaction data (from Kaggle)
│   └── train_identity.csv      ← IEEE-CIS identity data (from Kaggle)
│
├── models/                     ← Serialized model artifacts
│   ├── fraud_model.pkl
│   ├── scaler.pkl
│   └── label_encoders.pkl
│
├── charts/                     ← SHAP plots and evaluation charts
│
├── dashboard/
│   └── app.py                  ← Streamlit interactive dashboard
│
└── screenshots/                ← Dashboard preview images
```

---

## 🔄 Project Workflow

```
Data Loading → Preprocessing → Feature Engineering → SMOTE
     → LightGBM Training → Evaluation → SHAP XAI → Dashboard
```

### Step-by-step

1. **Data Collection** — Load transaction and identity CSVs; merge on `TransactionID`
2. **Preprocessing** — Handle missing values, drop low-signal columns, encode categoricals
3. **Feature Engineering** — Derive fraud-signal features (velocity, amount ratios, time deltas)
4. **SMOTE** — Synthesize minority-class samples to fix class imbalance before training
5. **Model Training** — Train LightGBM classifier with early stopping
6. **Evaluation** — Accuracy, Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix
7. **SHAP Explainability** — Summary plots, force plots, per-transaction explanations
8. **Dashboard Deployment** — Interactive Streamlit app for live prediction and analytics

---

## 🤖 Why LightGBM?

- ⚡ Extremely fast training speed on large datasets
- 🎯 High accuracy on tabular/structured data
- 💾 Memory-efficient leaf-wise tree growth
- 📊 Handles imbalanced datasets effectively
- 🔧 Easy hyperparameter tuning

---

## ▶️ How to Run

### Prerequisites
- Python 3.10+
- Dataset from Kaggle: [IEEE-CIS Fraud Detection](https://www.kaggle.com/c/ieee-fraud-detection/data)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/FraudDetection_Ayush.git
cd FraudDetection_Ayush
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the dataset

Download from Kaggle and place inside `data/`:
```
data/train_transaction.csv
data/train_identity.csv
```

### 4. Run the notebook

```bash
jupyter notebook analysis.ipynb
```

This will train the model and save artifacts to `models/`.

### 5. Launch the dashboard

```bash
cd dashboard
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📊 Dashboard Features

- 📌 **Fraud Overview Analytics** — Key fraud metrics and distributions
- 🔍 **Transaction Explorer** — Filter and drill into individual transactions
- ⚠️ **Live Fraud Prediction** — Input transaction features and get real-time risk score
- 📈 **Fraud Rate Analysis** — Time-based and feature-based fraud trends
- 🧠 **SHAP Visualizations** — Understand why a transaction was flagged

---

## 📁 Dataset

**IEEE-CIS Fraud Detection Dataset**

Available on Kaggle: [https://www.kaggle.com/c/ieee-fraud-detection](https://www.kaggle.com/c/ieee-fraud-detection/data)

> ⚠️ The dataset is not included in this repository due to Kaggle's terms of service. Download it directly and place the CSVs in the `data/` directory.

---

## 📸 Screenshots

> Run the app locally, take screenshots, save them inside the `screenshots/` folder, push to GitHub, then paste links below like this:

```
![Dashboard Home](screenshots/home.png)
![Fraud Prediction](screenshots/prediction.png)
![SHAP Visuals](screenshots/shap.png)
```

<!-- Once you've pushed screenshots, uncomment the lines above and delete this comment block -->

---

## 🚀 Future Improvements

- [ ] 🌐 REST API with FastAPI for real-time inference
- [ ] ☁️ Cloud deployment (AWS / GCP / Azure)
- [ ] 🤖 Deep learning models (TabNet, FT-Transformer)
- [ ] 🔐 Unsupervised anomaly detection (Isolation Forest, Autoencoder)
- [ ] 📱 Mobile-responsive dashboard
- [ ] 🔄 Real-time streaming with Kafka

---

## 💼 Use Cases

- 🏦 Banking fraud detection
- 💳 Payment gateway monitoring
- 📊 Financial risk analysis
- 📋 Insurance claim fraud detection
- 🛒 E-commerce transaction monitoring

---

## 👨‍💻 Author

**Ayush**
Machine Learning Enthusiast · Data Analytics & AI · Streamlit Dashboard Developer

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## ⭐ Like this project?

If this project helped you, please give it a **⭐ star** on GitHub — it helps others discover it!

**Contributions, issues, and feature requests are welcome!**
