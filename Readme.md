AI Individual Programming Assignment

This repository contains implementations of basic Artificial Intelligence programs including Turing Test simulation, CAPTCHA verification system, and a search problem (Missionaries and Cannibals).
Assignment Overview
Assignment	Topic	File
1	Turing Test Simulation	turingtest.py
1	CAPTCHA Verification	captcha.py
2	Missionaries and Cannibals Search Problem	missionaries_cannibals.py
1. Turing Test Simulation
The Turing Test, proposed by Alan Turing, is used to determine whether a machine can imitate human intelligence.
In this program:
A judge asks questions.
Both a bot and human responses are evaluated.
The judge analyzes the responses and decides whether they are from a human or a machine.
How to Run
python turingtest.py
Example Output
Q: What is your name?
Bot   : I process sentiment data.
Judge : BOT

Human : Hi! My name is Alex.
Judge : HUMAN
2. CAPTCHA Verification System
CAPTCHA (Completely Automated Public Turing Test to tell Computers and Humans Apart) is used to prevent automated bots from accessing systems.
This program generates different CAPTCHA challenges:
Math CAPTCHA – simple arithmetic problems
Logic CAPTCHA – general knowledge questions
Text CAPTCHA – typing randomly generated characters
How to Run
python captcha.py
3. Missionaries and Cannibals Problem
The problem involves three missionaries and three cannibals crossing a river using a boat that can carry only two people at a time.
Constraint:
Cannibals must never outnumber missionaries on either bank.
Goal:
Move all six individuals safely from the left bank to the right bank.
Algorithms Implemented
Algorithm	Description	Optimal
BFS	Explores nodes level by level using a queue	Yes
DFS	Explores deep paths first using a stack	Not guaranteed
IDDFS	Depth-limited DFS repeated with increasing depth	Yes
Running the Program
Run the search program using:
python missionaries_cannibals.py
Output Screenshots
BFS Output
DFS Output
IDDFS Output
Algorithm Comparison
(Screenshots included in the project files.)
Project Files
File	Description
turingtest.py	Turing Test implementation
captcha.py	CAPTCHA system implementation
missionaries_cannibals.py	BFS, DFS and IDDFS search implementation
output_bfs.png	Screenshot of BFS output
output_dfs.png	Screenshot of DFS output
output_iddfs.png	Screenshot of IDDFS output
output_comparison.png	Performance comparison
README.md	Project documentation
Requirements
Python 3
No external libraries required.
Conclusion
This assignment demonstrates how AI techniques can be applied to distinguish humans from machines and solve search problems using uninformed search algorithms.