# Artificial Intelligence for Physical Systems

This repository explores the implementation of autonomous behaviors for robots in simulated environments using the **ThinkingCap-II** simulator. The project covers the spectrum from purely reactive systems to hybrid (deliberative-reactive) architectures and Fuzzy Logic control.

## Projects & Exercises

### 1. Robot Roombo: Reactive Cleaning
* **Objective:** Efficient floor coverage in a 15x15m environment without a priori maps.
* **Mechanism:** Purely **reactive navigation**. The robot uses cell maps to track "cleaned" areas (white) and obstacles (black), aiming to minimize unexplored (grey) zones.
* **Implementation:** Behavior-based architecture for obstacle avoidance and area coverage.

### 2. Robot Minotaur: Maze Traversal (Reactive)
* **Objective:** Navigating and exiting a maze using a "wall-following" strategy (e.g., Right-Hand Rule).
* **Mechanism:** Reactive behavior where the robot maintains a reference distance to walls.
* **Analysis:** Study of failure points when losing the reference wall and comparison between left vs. right wall-following strategies.

### 3. Robot Minotaur++: Hybrid Navigation
* **Objective:** Finding the shortest path to a known destination in complex mazes with intersections.
* **Mechanism:** **Hybrid Architecture**. 
    * *Deliberative:* Environment modeling and path planning using cell maps.
    * *Reactive:* Obstacle avoidance and look-ahead point following.
* **Key Focus:** Optimization of look-ahead distance and sensor range to improve navigation efficiency.

## Tech Stack & Tools
* **Simulator:** ThinkingCap-II (Java-based architecture).
* **Control:** Fuzzy Logic (Fuzzy sets implemented for behavior definition).
* **Languages:** Java (robot behaviors), Python (visualization of Fuzzy sets).

## Repository Contents
* `Exercise-1/2/3/`: Source code (.java, .class, .arch) and **simulation videos** for each scenario.
* `iasf.b_fuzzy_sets.ipynb`: Python notebook visualizing the membership functions used in the robot's logic.
* `memoria.pdf`: Final report documenting the architectures, experiments, and results.

## AI Relevance
* **Hybrid Architectures:** Understanding the balance between low-level reaction and high-level planning.
* **Fuzzy Logic:** Applying non-binary logic to handle sensor uncertainty and smooth motor control.
* **Robotics Foundations:** Essential for autonomous vehicle navigation and industrial automation.
