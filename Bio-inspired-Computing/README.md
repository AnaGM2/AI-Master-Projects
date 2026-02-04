# Bio-Inspired Computing

This repository explores optimization and search algorithms inspired by biological processes. The focus is on **Evolutionary Algorithms (EA)**, genetic operators, and their application to different problems and feature engineering.

## Deliverable Projects

### 1. The N-Queens Problem: Evolutionary Approach
Implementation of an Evolutionary Algorithm using **permutation-based representation** to solve the classic N-Queens puzzle.
* **Comparison of Schemes:**
    * **EA1:** Proportional selection, stochastic universal sampling, and full generational replacement.
    * **EA2:** Exponential ranking selection ($c=0.99$), stochastic universal sampling, and full generational replacement.
* **Optimization:** Added early stopping criteria upon finding the global optimum to maximize computational efficiency.



### 2. Correlation-based Feature Selection (CFS) via EA
Design and implementation of an Evolutionary Algorithm as a search strategy for feature selection in high-dimensional datasets.
* **Technical Specifications:**
    * **Representation:** Binary strings (representing selected features).
    * **Operators:** Uniform crossover ($p_c=0.6$) and bit-flip mutation ($p_m=0.1$).
    * **Parameters:** Exponential ranking selection ($c=0.3$), 100,000 evaluations.
* **Validation:** Executed 10 independent runs with different seeds on the **ALL-AML_train** dataset.
* **Visualization:** Comparative plots showing the fitness evolution across all 10 runs to analyze algorithm stability and convergence.



## Tech Stack
* **Language:** Python
* **Key Libraries:** `NumPy` (population matrix operations), `Matplotlib` (convergence plots), `Pandas`.
* **Core Concepts:** Genetic Operators (Crossover, Mutation), Fitness Function Design, Selection Pressures.

## Repository Contents
* `Class-Practices/`: Small-scale notebooks and exercises covering PSO (Particle Swarm Optimization), Ant Colony, and basic Genetic Algorithms.
* `Deliverables/`: Comprehensive solutions for the N-Queens and CFS problems, including code and performance analysis.

## AI Relevance
* **Optimization:** EAs are crucial when the search space is too large for gradient descent or exhaustive search.
* **Feature Engineering:** Automated feature selection (like in Practice 2) is a key step in building efficient Machine Learning pipelines, reducing dimensionality, and preventing overfitting.
