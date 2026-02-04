# Explainable Machine Learning (XAI)

This repository focuses on **Interpretable AI**, moving beyond "black-box" models to understand the logic behind algorithmic predictions.


## Main Project: Predicting Academic Success
This project applies XAI methods to classification models trained on student performance data. The objective was to identify the key factors that lead to academic success or failure.

* **Task:** Classification (Success vs. Failure).
* **Models:** Implementation of various classifiers (Decision Tree, XGBoost, SVM).
* **XAI Techniques Applied:** SHAP, LIME, Tree Visualization, Feature Importane.
    * **Global Explanations:** To understand the model's overall behavior.
    * **Local Explanations:** To explain individual student predictions.
* **Outcome:** Technical presentation (PDF) summarizing how specific factors influence the final prediction.


## Class Practices & Exercises
A collection of short-form exercises covering different interpretability frameworks:
* **Python Notebooks:** Manual implementation of intrinsically interpretable models and post-hoc explanation libraries.
* **Orange Workflows (`.ows`):** Visual programming approach to Machine Learning, focusing on data exploration and model evaluation without extensive coding.

## Tech Stack
* **Language:** Python
* **Tools:** Orange Data Mining.
* **Key Libraries:** `SHAP`, `LIME`, `NumPy`, `Scikit-Learn`, `Matplotlib`, `Pandas`.

## AI Relevance
* **Trust & Ethics:** Essential for deploying AI in sensitive sectors like Education, Healthcare, or Finance.
* **Model Debugging:** Using XAI to detect biases the model might be taking during training.
* **Regulatory Compliance:** Aligning with the "Right to Explanation" requirements in modern AI regulations.
