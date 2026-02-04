# Explainable Machine Learning (XAI)

This repository focuses on **Interpretable AI**, moving beyond "black-box" models to understand the logic behind algorithmic predictions.


## Main Project: Predicting Academic Success

* **Context:** Developed a classification model to predict whether a university student will succeed, fail, or drop out.
* **Objective:** Beyond prediction, the project identifies the *key factors* (socio-economic, academic, and personal) that drive these outcomes using XAI techniques.
* **XAI Techniques Applied:** * **Global Explanations:** Feature Importance and Partial Dependence Plots (PDP) to understand the general behavior of the model.
    * **Local Explanations:** (e.g., LIME or SHAP) to explain specific individual student cases.
* **Deliverables:** Comprehensive Python Notebook and a PDF presentation summarizing the findings.



## Class Practices & Exercises
A collection of short-form exercises covering different interpretability frameworks:
* **Python Notebooks:** Implementation of intrinsic interpretable models (Decision Trees, Logistic Regression) vs. post-hoc explanations for complex models (Random Forests, XGBoost).
* **Orange Workflows (`.ows`):** Visual programming approach to Machine Learning, focusing on data exploration and model evaluation without extensive coding.

## Tech Stack
* **Language:** Python
* **Tools:** Orange Data Mining.
* **Key Libraries:** `SHAP`, `LIME`, `InterpretML`, `Scikit-Learn`, `Matplotlib`.

## AI Relevance
* **Trust & Ethics:** Essential for deploying AI in sensitive sectors like Education, Healthcare, or Finance.
* **Model Debugging:** Using XAI to detect biases or "shortcuts" the model might be taking during training.
* **Regulatory Compliance:** Aligning with the "Right to Explanation" requirements in modern AI regulations.
