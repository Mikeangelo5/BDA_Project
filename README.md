# BDA Project: Educational Disparities in Access to Essential Services

## 🔍 Project Overview

This project investigates how the education level of household heads in Estonia (2010–2012) influences the average distance to essential services like schools, shops, post offices, and public transport. The aim is to identify potential socio-spatial inequalities using open government data and interpretable machine learning techniques.

## ⚙️ Key Features

* Data retrieval via Statistics Estonia API (LET300 table)
* Exploratory Data Analysis (EDA) using boxplots, line plots, and heatmaps
* Supervised ML models for regression and classification:

  * Regression: Linear, Ridge, Random Forest
  * Classification: Random Forest, Logistic Regression
* Feature importance visualization
* Performance evaluation with cross-validation, RMSE, R², accuracy, F1-score

## 📃 Dataset

* Source: [Statistics Estonia (LET300 Table)](https://andmed.stat.ee/en/stat/LET300)
* Timeframe: 2010–2012
* Features: Education level of household head, type of service, year, and average distance (km)

## 💡 Methodology

* Data Cleaning and Restructuring (JSON-stat2 to tabular form)
* Label encoding of categorical features
* Regression models to predict numeric distance
* Classification models to categorize distances: Short (<2 km), Medium (2–3.5 km), Long (>3.5 km)
* Evaluation Metrics:

  * Regression: R² Score, RMSE
  * Classification: Accuracy, Precision, Recall, F1-Score, Confusion Matrix

## 💡 Insights

* Education level and type of service were key predictors of distance
* Random Forest Regression achieved R² ≈ 0.97 (RMSE = 0.19)
* Random Forest Classifier achieved 73% accuracy
* Logistic Regression achieved 68% accuracy
* Strong classification performance for "Medium" distance group

## 🚧 Challenges & Solutions

**Challenges:**

* Limited dataset (no geographic or socioeconomic variables)
* Data imbalance across education levels and services

**Solutions:**

* Applied label encoding and category grouping for balance
* Used cross-validation and two model types (regression + classification)

## 🚿 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Mikeangelo5/BDA_Project.git
cd BDA_Project
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the notebook or main script:**
   Use the `BDA_Project.ipynb` notebook for step-by-step execution.

## 🔍 Tools Used

* Python 3.x
* Pandas, NumPy
* Seaborn, Matplotlib
* Scikit-learn

## 👥 Contributors

* Yagub Hajiyev
* Elchin Huseynov

## 📅 License

This project is licensed under the [MIT License](./LICENSE).

---

*For questions or feedback, feel free to open an issue or contact the contributors via GitHub.*
