# Master's Thesis

## Study of Monte Carlo and Monte Carlo Tree Search Techniques Applied to Reinforcement Learning in Strategy Games

This Master's Thesis focuses on the study and implementation of decision-making algorithms in strategy games, with a particular emphasis on methods based on Monte Carlo and Monte Carlo Tree Search (MCTS).

The work begins with an introduction briefly outlining the research objectives. Following this, it delves into the general concepts of Game Theory, including definitions and examples, while presenting various game representations such as normal form and extensive form. Furthermore, the selected algorithms for analysis are detailed, along with several selection policies used in MCTS, such as $\epsilon$-greedy, UCB, and Softmax.

Subsequently, experiments and simulations are conducted across four classic strategy games: Nim, Connect 4, Othello, and Go. For each game, simulations are performed by pitting Monte Carlo agents against a human player to better understand the game logic. This is followed by comparative analyses between the different implemented agents, facing them against each other in pairs. Additionally, a debugging tool based on tree diagrams was developed for MCTS, facilitating the analysis and comprehension of algorithmic behavior, especially in simpler games that are easier to visualize.

Finally, the results are discussed, and conclusions are drawn regarding the efficacy and applicability of the studied techniques. The appendices include details on the Python implementation of the algorithms, selection policies, games, and the debugging tool.

Ultimately, this work delves into the field of Artificial Intelligence applied to strategy games and provides relevant results concerning their development and evaluation.

### Tech Stack

* **Language:** Python.
* **Format:** Jupyter Notebooks (.ipynb)
