## MATH 341: Python Assignment 2

This assignment will involve using and modifying some Classes in the `hw_two_utils.py` file.

First, import `Card` and `CardDeck` and understand how to use them.  
Sample code has been provided in `02_python_assignment.py`.

### Problem 1: 
Figure out how to simulate shuffling and dealing the `n_cards` top cards from a `CardDeck` object.  
This could be done in a few ways, either by modifying the class itself to add a `shuffle_and_deal` method 
or by creating a `CardDeck` object as it is and doing all of the shuffle and deal logic in 
`problem_one(n_cards)`.  In either case, `problem_one(n_cards)` should return a list of `n_cards` random `Cards`.

### Problems 2-5 refer to straight five-card poker.  
In this variant, you must play the five cards you were dealt.  You cannot discard and draw new cards.  
Use your method from problem one to estimate the following probabilities.  Note that:
* Two of a kind for this problem means "at least two of a kind" and three or four matching cards qualifies.
* Flush is any time all five cards match suit, including Royal and straight flushes.

### Problem 2: 
Write a method to estimate the probability of being dealt at least two of a kind in straight 5-card poker.

### Problem 3:
Write a method to estimate the probability being dealt any type of flush in straight 5-card poker.

### In problems 4 and 5, you will repeat the above analysis for HyperPoker.  

First fill in the template for a `HyperCardDeck` to create an unshuffled deck of 55-cards.  
* The deck has five suits - the standard four and then the `Horseshoes` suit
* Each suit has the standard face cards `JQK` and `Ace` through `8`.

Next repeat whatever you did for the standard deck to create a method to shuffle and deal `n_cards` off 
the top of a HyperDeck.

### Problem 4: 
Write a method to estimate the probability of being dealt at least two of a kind in straight 5-card HyperPoker.

### Problem 5:
Write a method to estimate the probability being dealt any type of flush in straight 5-card HyperPoker.

### Problem 6:
Use the provided `plot_convergence_curves` method to visualize how the experimental probabilities you estimated in 
problems 2, 3, 4, and 5 converge to the true values as more and more trials are performed.  
You may need to do some tweaking of the imports or syntax here depending on whether you're using a standard IDE 
or Jupyter notebook.