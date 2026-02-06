# Machine Learning Extensions: Reinforcement Learning & Federated Learning

This course explores advanced paradigms in Machine Learning: **Reinforcement Learning (RL)** for autonomous decision-making and **Federated Learning (FL)** for decentralized, privacy-preserving model training.

---

## Part 1: Reinforcement Learning (RL)
Focuses on how agents learn to make decisions by interacting with an environment to maximize rewards.

* **K-Armed Bandits:** A comparative study of exploration vs. exploitation strategies (Epsilon-greedy, UCB, etc.) in the classic bandit problem.
* **Complex Environments:** Application of RL algorithms to high-dimensional state spaces, analyzing convergence and stability in simulated environments.
* **Outputs:** Detailed experimental reports (.pdf) and implementation notebooks for both scenarios.



---

## Part 2: Federated Learning (FL) with Nebula
Extensive experimental work on decentralized AI using the **Nebula** framework within a Virtual Machine environment.

### Experimental Tasks:
1. **CFL vs. DFL:** Comparative analysis of Centralized and Decentralized Federated Learning using CNNs on the **CIFAR-10** dataset, evaluating **IID vs. Non-IID** data distributions.
2. **Adversarial Attacks:** Simulating **Model Poisoning** (Gaussian noise) and **Label Flipping** attacks with varying percentages of malicious nodes.
3. **Robust Aggregation:** Implementation of defense algorithms like **Trimmed Mean** and **Krum** to mitigate malicious updates.
4. **Reputation Systems:** Evaluation of Static vs. **Dynamic Weighting** reputation systems to isolate malicious participants and improve global model stability.
5. **Model Optimization:** Improving transmission efficiency using **Pruning** ($l1$ unstructured) and **Quantization** (bf16-mixed vs. 64-true precision).



## Tech Stack
* **RL:** Python, Gymnasium.
* **FL:** **Nebula** (Federated Learning framework).
* **Specialized Tools:** Virtual Machines for distributed simulation.

## AI Relevance
* **Privacy:** FL is essential for industries with sensitive data (Healthcare, Finance) where data cannot leave its source.
* **Security:** Understanding adversarial ML is critical for building resilient AI systems.
* **Efficiency:** Knowledge of pruning and quantization is key for deploying AI on different devices.
