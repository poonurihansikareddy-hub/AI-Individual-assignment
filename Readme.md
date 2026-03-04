AI Programming Assignments
Programming Individual Assignment

Assignment Overview
Assignment	Topic	Files
1	Turing Test and CAPTCHA	turingtest.py, captcha.py
2	Missionaries and Cannibals Search	missionaries_cannibals.py
Assignment 1: Turing Test (turingtest.py)
This program simulates the Turing Test, where a judge tries to determine whether responses are given by a human or a machine.
Components
BotPlayer — generates machine-like responses
Judge — analyzes responses and decides HUMAN or BOT
If suspicion score ≥ 40 → classified as BOT.
How to Run
python turingtest.py
Sample Output
Q: Do you have feelings?
Bot   : I process sentiment data.
Judge : BOT (suspicion: 40%)

Human : Yes, I feel happy, sad, excited.
Judge : HUMAN (suspicion: 0%)
Assignment 1: CAPTCHA (captcha.py)
This program implements a CAPTCHA system used to differentiate humans from bots.
CAPTCHA Types
Type	Example	Purpose
Math	Solve: 14 + 7 = ?	Arithmetic
Logic	What comes after Tuesday?	Common knowledge
Text	Type: RXWQP	Character recognition
How to Run
python captcha.py
Sample Output
Type      : Math CAPTCHA
Challenge : Solve: 5 + 9 = ?
Answer    : 14

PASS - Human verified
Assignment 2: Missionaries and Cannibals (missionaries_cannibals.py)
Three missionaries and three cannibals must cross a river using a boat that can carry a maximum of two people.
Constraint: Cannibals must never outnumber missionaries on either bank.
Goal: Move everyone safely from the left bank to the right bank.
Algorithms Implemented
Algorithm	Strategy	Optimal?	Memory
BFS	Queue, level by level	Yes	Higher
DFS	Stack, deepest first	Not guaranteed	Lower
IDDFS	Repeated depth-limited DFS	Yes	Lower
How to Run
python missionaries_cannibals.py
Sample Output
0. Left[3M 3C] <boat> ~~~~ Right[0M 0C]
1. Left[3M 1C] ~~~~ <boat> Right[0M 2C]
...
11. Left[0M 0C] ~~~~ <boat> Right[3M 3C]

Algorithm    Steps   Nodes   Time(ms)
BFS             11      15      0.04
DFS             11      12      0.03
IDDFS           11      66      0.25
Files
File	Description
turingtest.py	Turing Test simulation
captcha.py	CAPTCHA system implementation
missionaries_cannibals.py	BFS, DFS, IDDFS search problem
output_bfs.png	BFS output screenshot
output_dfs.png	DFS output screenshot
output_iddfs.png	IDDFS output screenshot
output_comparison.png	Algorithm comparison screenshot
README.md	Documentation
Requirements
Pure Python 3
No external libraries required.