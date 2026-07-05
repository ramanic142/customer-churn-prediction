# 📊 Customer Churn Prediction

An end-to-end machine learning project that predicts whether a telecom customer is likely to cancel their subscription (churn), using their account and service usage data. Includes a live interactive web app for real-time predictions.

## 🎯 Business Problem

Customer churn — when a customer stops using a company's service — is one of the most costly problems for subscription-based businesses. Acquiring a new customer typically costs far more than retaining an existing one, making early churn prediction a high-value tool for retention teams.

This project builds a model that identifies at-risk customers *before* they leave, based on patterns in their contract type, service usage, billing, and tenure.

## 🛠️ Tools & Tech Stack

- **Python** — data cleaning, exploration, and machine learning
- **SQL (SQLite)** — structured data storage and querying
- **Streamlit** — interactive web app for live predictions
- **scikit-learn** — model training and evaluation
- **pandas, matplotlib** — data manipulation and visualization

## 📁 Project Structure
## 🔍 Key Insights from Data Exploration

- **Contract type is the strongest churn driver**: month-to-month customers churn at **42.7%**, compared to just **11.3%** for one-year and **2.8%** for two-year contracts.
- **Fiber optic internet customers churn at 41.9%**, more than double DSL customers (19.0%).
- **Tenure matters**: churned customers averaged just **18 months** as customers, versus **37.6 months** for those who stayed.

## 🤖 Model Performance

Trained and compared Logistic Regression and Random Forest classifiers. Logistic Regression was selected for its comparable performance and superior interpretability.

| Metric | Score |
|--------|-------|
| Accuracy | 80.0% |
| Precision | 64.4% |
| Recall | 55.1% |
| ROC-AUC | **0.841** |

**Top predictive features** (after feature scaling): tenure, monthly charges, and contract type — consistent with the exploratory findings above.

## 🚀 Live App

Try the live prediction app here: **[Link coming soon]**

Enter a hypothetical customer's details and get an instant churn risk prediction with probability score.

## ⚙️ Running Locally

```bash
# Clone the repo
git clone https://github.com/ramanic142/customer-churn-prediction.git
cd customer-churn-prediction

# Install dependencies
pip install -r requirements.txt

# Load data into SQLite
python src/load_data.py

# Run the app
cd app
streamlit run app.py
```

## 📈 Dataset

[Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) — 7,043 customers, 21 features, sourced from Kaggle.