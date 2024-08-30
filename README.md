# Applied AI - Batch A 🦾

This repository contains lecture notes, code examples, and interactive demos for various topics in AI and programming demonstrated in class. 
Below, you'll find a list of topics covered along with links to relevant resources.

## Setting up Environment 
- Create a conda virtual environment: `conda create --name aai_code python=3.12`
- Activate the enviroment: `conda activate aai_code`
- Install requirements in environment: `pip install -r requirements.txt`

## Topics and Resources

### Topic 1: Object Oriented Programming

- **Lecture Notes**: [Object Oriented Programming - Lecture Notes](https://github.com/yash161101/Applied-AI-Batch-A/blob/main/oops/oop_notes.ipynb)
  - Comprehensive notes covering the fundamentals of Object Oriented Programming (OOP). This resource will help you understand key OOP concepts such as classes, objects, class methods, and inheritance.

- **Kaggle Example - Titanic Problem**: [Titanic Problem Solved with OOP](https://www.kaggle.com/code/yash161101/topic-1-object-oriented-programming)
  - An example demonstrating how to apply Object Oriented Programming principles to solve the Titanic problem on Kaggle. This example showcases the practical application of OOP in data science and machine learning projects.

### Topic 2: Search

- **Lecture Notes**: [Search - Lecture Notes](https://github.com/yash161101/Applied-AI-Batch-A/blob/main/search/search_notes.ipynb)
  - A collection of generic code snippets for implementing various search algorithms. This resource provides a foundational understanding of how to code search algorithms from scratch.

- **Search Algo Demo**: [Search Algorithm Demo](https://github.com/yash161101/Applied-AI-Batch-A/tree/main/search/search_algo_demo)
  - An interactive interface that creates a maze and visualizes how Depth-First Search (DFS), Breadth-First Search (BFS), and A* search algorithms work in action. This demo is designed to help you understand how these search algorithms operate in a controlled environment.
  - To run this use `python > 3.12` and use the command `python main.py`

- **Map Example**: [Search Algorithms with a Map of Paris](https://github.com/yash161101/Applied-AI-Batch-A/tree/main/search/map_example)
  - A practical example illustrating search algorithms applied to a real-world scenario using a map of the streets of Paris. This example demonstrates how search algorithms can be used to navigate and find paths in geographical data.

- **tictactoe**: [Adversarial Search with Tic-Tac-Toe](https://github.com/yash161101/Applied-AI-Batch-A/tree/main/search/tictactoe)
  - An interactive example explaining adversarial search through a Tic-Tac-Toe game. This resource includes an interface that shows how algorithms can be used to play optimally in adversarial environments.
  - To run this use the command `python runner.py`

### Topic 3: Knowledge
- **knights**: [Knights and Knaves Problem](https://github.com/yash161101/Applied-AI-Batch-A/tree/main/knowledge/knights)
  - The Knights problem is based on the classic "Knights and Knaves" logic puzzles. In these puzzles, characters are either knights, who always tell the truth, or knaves, who always lie. The objective is to use propositional logic to determine the identity (knight or knave) of each character based on the statements they make. The AI uses a model-checking algorithm to evaluate the truthfulness of these statements and deduce the correct identities of the characters
  - To run this use the command `python puzzle.py`

### Topic 4: Uncertainty
- **Batman Network**: [Bayesian Networks Explained - Batman Example](https://github.com/yash161101/Applied-AI-Batch-A/blob/main/uncertainty/bayesian_network.ipynb)
  - An example using pomegranate library demonstrating how Bayesian Networks can be constructed and be used to create inferences and calculate probabilities of states.

- **Markov Chain Demo**: [Markov Chain Demo - Stocks Example](https://github.com/yash161101/Applied-AI-Batch-A/blob/main/uncertainty/markov_chain.ipynb)
  - The code simulates stock price movements using a basic random walk model, with daily returns drawn from a normal distribution. It visualizes multiple simulations of stock price trajectories over time, demonstrating the variability and potential paths prices can take.
  
### Topic 5: Optimization
- **Hospitals**: [Hill Climbing Explained - Hospitals Example](https://github.com/yash161101/Applied-AI-Batch-A/tree/main/optimization/hospitals)
  - An example demonstrating how Hill Climbing and Random Hill Climbing works by adding random houses to a grid and finding the optimized way to place n number of hospitals such that they are the closest to all the houses.
  - To run this use the command `python hospitals.py`

- **IPL Team Selection**: [Linear Programming - IPL Team Selection Example](https://github.com/yash161101/Applied-AI-Batch-A/tree/main/optimization/ipl_example)
  - This code takes 20 random players and tries to maximize the team performance by keeping in mind the constraints such as budget, team balance and overseas limit to find the best posible team.
  - To run this use the command `python ipl_team_selection.py`

Happy Coding!
