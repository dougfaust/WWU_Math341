## MATH 341: Python Assignment 3

This assignment will involve using the pandas module for data exploration and manipulation in python.

First, make sure that pandas is installed in your environment. 

### Problem 1: 
Load the `` csv file located here by passing the url as your function argument. 

For some of these problems, we don't care about the position Left Wing (`LW`) or Right Wing (`RW`) separately, 
so make a new column in the DataFrame called `Position_type` so that both of those position categories are 
coded as `W` in the `POS` column.  Return this new, augmented DataFrame with both position columns.


### Problem 2: 
Write a method to return the top N players in some numerical category.  
Your method should include code (control flow) that returns `None` and surfaces a polite message or Error if the 
user requests a statistic that isn't in the list of numerical columns.

### Problem 3:
Write a method to find the conditional probability that a player scores > N goals if they are a Center, Wing, 
or Defenseman.

### Problem 4: 
Write a method that takes in your DataFrame and prints out the answer to the following question: 
"What's the probability that player is Center, Wing, or Defenseman given they scored more than 10 goals in the 23-24 Season?"

### Problem 5:
Create a Fantasy team based on some *quantitative* criteria (i.e. "I <3 Detroit" is not quantitative).  
Your team should consist of 4 Centers, 4 Left Wings, 4 Right Wings, and 6 Defensemen.  The `problem_five` method 
should take in a DataFrame like the one your created in Problem 1 and return a DataFrame with a row for each member 
of your Fantasy team.

Clearly describe your methodology for selecting players.  This won't be graded on the particular choice of methodology, 
but rather whether or not your code accurately instantiates that methodology.  
