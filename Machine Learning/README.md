# Machine Learning

This repository contains two major practical projects focusing on solving complex real-world problems using Supervised Learning and Multivariate Time Series Analysis.

## Practice 1: Advanced Classification Tasks
Three distinct challenges aimed at mastering specific data issues:

### 1. Imbalanced Data (CocheRadar)
* **Challenge:** High class imbalance in vehicle identification (Car vs. Other).
* **Techniques:** Application of resampling methods (SMOTE, Under/Over-sampling) and robust metrics like F1-Score and AUC-ROC to handle skewed distributions.

### 2. Multi-label Classification (Water Quality)
* **Challenge:** Predicting multiple taxa present in a single water sample simultaneously.
* **Techniques:** Implementation of Problem Transformation (Binary Relevance, Classifier Chains) and Algorithm Adaptation methods.

### 3. Ensemble Learning (Credit Card Approval)
* **Challenge:** Building a high-performance model for credit risk assessment.
* **Techniques:** Comparison between classic classifiers and **Ensemble Methods** (Random Forest, Gradient Boosting, XGBoost).



---

## Practice 2: Multivariate Time Series Forecasting (NOx)
Predicting Nitrogen Oxide (NOx) levels with a **7-day horizon** using a multi-year sensor dataset (2017-2022).

* **The Dataset:** High-resolution (hourly) data combining **Air Quality** (SO2, O3, PM10, Benzene) and **Meteorological variables** (Temperature, Wind Speed, Solar Radiation).
* **Key Tasks:**
    * **Feature Engineering:** Creating lag variables, rolling windows, and handling temporal dependencies.
    * **Correlation Analysis:** Understanding the influence of weather patterns on pollutant concentration.
    * **Modeling:** Multi-step regression to forecast the next 168 hours (7 days) of NOx emissions.



## Tech Stack
* **Language:** Python.
* **Libraries:** `Scikit-learn`, `XGBoost`, `LightGBM`, `Pandas`, `Matplotlib`, `Seaborn`.


## AI Relevance
This course bridges the gap between academic theory and industrial application by focusing on **Explainability and Problem-Solving** (why a model works and how to fix data leakage or overfitting) rather than just "accuracy chasing".
