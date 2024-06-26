## MATH 341: Python Assignment 1

For problems 1, 2, and 3, use the function `generate_random_set(min_val, max_val, set_length)` to generate input sets.  Verify that the function parameters mean what you think they mean. 

### Problem 1: 
Write a python method with signature `problem_one(A, B, C)` that calculates $(A \cap B) \cup C$.

### Problem 2: 
Write a python method with signature `problem_two(A, B, C)` that calculates $(A \cup C) \cap (B \cup C)$.

### Problem 3:
Use your code from Problems 1 and 2 to write a python method `problem_three(A, B, C)` to return `True` 
if $(A \cup C) \cap (B \cup C) = (A \cap B) \cup C$ and `False` if not.  
Test your method by looping over some random triplets of sets and explain what you observe (or don't observe).

### Problem 4: 
Experiment with the method `generate_rock_paper_scissors(rounds)` which has been provided.  
Use, hack, be inspired by etc. this code to write a method `problem_four(games)` that does the following:

Given that a game of rock-paper-scissors (RPS) continues if there's a tie, 
the average number of rounds in an RPS game is greater than one.  
Write a method to estimate the average number of rounds in an RPS game.

### Problem 5: 
An easy way to plot a histogram is to use the `matplotlib.pyplot` module.

* The code
```
import random
import matplotlib.pyplot as plt

data = [random.randint(1, 100) for _ in range(300)]
plt.hist(data)
```
plots a histogram of 300 random integers chosen from in between 1 and 100


* The code
```
import numpy as np
import matplotlib.pyplot as plt

def sum_of_terms(min_val, max_val, number):
  return sum(np.random.randint((max_val-min_val+1), size=number) + min_val)

plt.hist([sum_of_terms(0, 10, 5) for _ in range(300)])
```
plots a histogram of 300 experiments where random 5 integers between 0 and 10 are picked and added together.

Write a method `problem_five(number_of_games)` that plots a histogram of the lengths of `number_of_games` different RPS games.

Comment on how that distribution looks compared to the distributions you see in the histograms generated by the two code examples given above.
