# Knowledge and Approximate Reasoning

This repository explores how AI models handle imprecise, uncertain, and structured knowledge using Semantic Technologies, Fuzzy Logic, and Probabilistic Graphical Models.

## Key Modules & Projects

### Chapter 2. Domain Ontologies (Semantic Web)
* **Project:** Design of a formal ontology for **Sustainable Water Management in Agriculture**.
* **Specifications:** Created using **Protégé**, including 50+ concepts/instances and predicate logic axioms.
* **Features:** Implementation of taxonomic hierarchies, non-taxonomic relations, and consistency checking using **BabelNet**.
* **Advanced Logic:** Use of fuzzy linguistic variables (adjectives/adverbs) within the ontological structure.


### Chapter 3. Fuzzy Logic: Holdridge Life Zones Zonifier
* **Project:** A fuzzy expert system that determines the **Holdridge Life Zone** of any point on Earth based on bioclimatic data.
* **Tasks:**
    * Design of membership functions for climate variables (Biotemperature, Precipitation, Humidity).
    * Implementation of a fuzzy inference system in Python.
    * **Visualization:** Generation of colored maps representing ecological zones from weather station datasets.


### Chapter 4. Reasoning under Uncertainty
* **Bayesian Networks:** Probabilistic inference and modeling of complex dependencies (e.g., medical diagnosis).
* **Evidence Theory:** Implementation of **Dempster-Shafer Theory** for combining evidence from multiple sources.
* **Certainty Factors:** Rule-based reasoning with uncertainty measures.


### Chapter 5. Soft Computing & Model Learning
* **Frost Prediction (FID3.5):** Using the FID3.5 algorithm to induce fuzzy decision trees.
    * **Objective:** Predict frost events ($T \le 0°C$) with a 2-hour lead time using meteorological sensor data (Jumilla, Spain).
    * **Analysis:** Study of fuzzy partitioning and manual inference validation vs. software results.
* **Bayesian Learning:** Learning structure and parameters for Bayesian Networks from data (Cancer and Energy consumption datasets).

## Tech Stack
* **Semantic Tools:** Protégé, BabelNet API.
* **Programming:** Python.
* **Specialized Software:** FID3.5 (Fuzzy Induction of Decision Trees).

## AI Relevance
* **Explainability:** Fuzzy systems and ontologies provide AI that humans can easily understand.
* **Robustness:** These techniques allow models to function correctly even when input data is noisy, incomplete, or ambiguous.
* **Expert Systems:** This approach is fundamental for building decision-support systems in specialized fields like Agriculture, Medicine, and Meteorology.
