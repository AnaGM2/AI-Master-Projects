# RL_GGM
Second assignment for the Reinforcement Learning (RL) subject.

## Information
- **Students:** Gil, Ana; García, José María; Malest, Levi.
- **Subject:** Machine Learning Extensions.
- **Academic Year:** 2024/2025
- **Group:** GGM
 
## Description
This repository has been created to conduct a comparative study between different classical reinforcement learning algorithms applied to the problem of learning in complex environments.
It contains an experiment report in ``.pdf`` format and other ``.py`` and ``.ipynb`` files that support the contents presented in the report. 

## Structure
- /docs/ $\hspace{0.1 cm}$ Contains the ``.pdf`` files
- /src/  $\hspace{0.42 cm}$ Contains the python scripts ``.py``, organized into the following subfolders:
  
  - ./agents/ $\hspace{0.2 cm}$ --> $\hspace{0.15 cm}$ Here we find the different classes developed to model the agents
  - ./memories/ $\hspace{0.2 cm}$ --> $\hspace{0.15 cm}$ Here we find a class developed to model a memory for Deep Q-Learning
  - ./networks/ $\hspace{0.2 cm}$ --> $\hspace{0.15 cm}$ Here we find a script with the neural network used in Deep Q-Learning
  - ./policies/ $\hspace{0.2 cm}$ --> $\hspace{0.15 cm}$ Here we find the decision policies used by the agents
  - ./wrappers/ $\hspace{0.2 cm}$ --> $\hspace{0.15 cm}$ Here we find the implementation of various wrappers for the environments used

## Installation and Use
Through ``main.ipynb``, you can navigate between the different notebooks contained in this repository simply by clicking the links provided there (see section **[2]**).
All these notebooks are ready to run on Google Colab without the need for any prior installation steps.

## Technologies Used
- Environment: Jupyter Notebooks (Google Colab)
- Programming Languages: Python (100%)
