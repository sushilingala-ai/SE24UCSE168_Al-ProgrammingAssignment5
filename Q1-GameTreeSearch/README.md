# Q1 – Game Tree Search Algorithms

## Problem Statement

Implement the Minimax Search algorithm, Alpha-Beta Search, Heuristic Alpha-Beta Search, and Monte-Carlo Tree Search (MCTS). Demonstrate their working using a game environment and provide test cases to support the correctness of the implementation.

---

## Approach

This project implements four classical game tree search algorithms using **Tic-Tac-Toe** as the test environment.

The game state is represented using a 3×3 board where:

* `X` represents the maximizing player
* `O` represents the minimizing player
* Empty cells represent available moves

The implemented algorithms are:

### 1. Minimax Search

Minimax performs an exhaustive search of the game tree assuming both players play optimally.

* MAX player attempts to maximize the utility value.
* MIN player attempts to minimize the utility value.
* Explores all possible game states until terminal positions are reached.

### 2. Alpha-Beta Search

Alpha-Beta Search improves Minimax by pruning branches that cannot affect the final decision.

* Uses Alpha (α) and Beta (β) bounds.
* Produces the same optimal result as Minimax.
* Significantly reduces the number of nodes explored.

### 3. Heuristic Alpha-Beta Search

A depth-limited version of Alpha-Beta Search.

* Uses a heuristic evaluation function when the depth limit is reached.
* Avoids exploring the complete game tree.
* Suitable for larger games where exhaustive search is impractical.

The heuristic evaluates board positions by assigning scores based on:

* Two-in-a-row opportunities
* One-in-a-row opportunities
* Potential winning lines
* Blocking opponent advantages

### 4. Monte-Carlo Tree Search (MCTS)

MCTS uses simulation-based search instead of exhaustive evaluation.

The algorithm consists of four phases:

1. Selection
2. Expansion
3. Simulation (Rollout)
4. Backpropagation

MCTS estimates move quality using repeated random simulations and the UCT (Upper Confidence Bound for Trees) strategy.

---

## Files

| File                   | Description                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| `search_algorithms.py` | Implementation of Minimax, Alpha-Beta, Heuristic Alpha-Beta, and Monte-Carlo Tree Search using Tic-Tac-Toe |

---

## Setup

Run the program:

```bash
python search_algorithms.py
```

---

## Running the Program

The program automatically:

1. Executes the complete test suite.
2. Displays PASS/FAIL results for all test cases.
3. Performs a performance comparison of all algorithms.

Example output:

```text
RUNNING TEST SUITE

[PASS] Minimax: perfect play from empty = draw
[PASS] AlphaBeta: same value as Minimax
[PASS] HeuristicAB depth=2: finds winning move
[PASS] MCTS: returns valid move from empty

RESULTS: 28/30 tests passed
```

A performance comparison is also displayed showing:

* Move selected
* Evaluation value
* Nodes explored
* Execution time

---

## Test Cases Implemented

The implementation includes multiple test cases to verify correctness and performance.

### Tic-Tac-Toe Engine Tests

* X wins on a row
* O wins on a column
* Draw detection
* Terminal state verification

### Minimax Tests

* Perfect play from empty board results in a draw
* Detection of immediate winning moves
* Blocking opponent winning moves
* Node exploration verification

### Alpha-Beta Tests

* Consistency with Minimax results
* Validation on randomly generated game states
* Comparison of node counts with Minimax
* Winning move detection

### Heuristic Alpha-Beta Tests

* Valid move generation at different depths
* Winning move detection with shallow search
* Heuristic evaluation validation
* Comparison of nodes explored at different depth limits

### Monte-Carlo Tree Search Tests

* Legal move generation
* Win-rate estimation
* Winning move selection
* Blocking move evaluation
* Performance against a random opponent

### Cross-Algorithm Tests

* Agreement between Minimax and Alpha-Beta
* Legal move generation by all algorithms
* Consistency checks across implementations

---

## Performance Analysis

The program compares all implemented algorithms on the same Tic-Tac-Toe board configuration.

Metrics reported:

| Metric         | Description                     |
| -------------- | ------------------------------- |
| Move           | Selected move                   |
| Value          | Utility or heuristic evaluation |
| Nodes Explored | Number of states evaluated      |
| Time           | Execution time in milliseconds  |

This comparison highlights the trade-off between optimality and computational efficiency.

---

## Project Structure

```text
Q1-GameTreeSearch/
├── search_algorithms.py
└── README.md
```

---

## Author

Sushanth Lingala
Roll No: **SE24UCSE168**
Course: **CS-2201 – Artificial Intelligence**
