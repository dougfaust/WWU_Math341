# -*- coding: utf-8 -*-
"""Math 341 tutorial 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bqz44hcfzMBOAPj6NP6gEzPLU7llz3lG
"""

# Creating sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

universal_set = {1, 2, 3, 4, 5, 6, 7}

# a list
print(type([1,2,2,1,2,1,1,1,2,1]))

# tuple (static)
print(type((1,2,2,1,2,1,1,1,2,1)))

# casting a list to a set - what happens?
set_c = set([1,2,2,1,2,1,1,1,2,1])

print(type(set_c))

print(set_c)

print("Initial sets:")
print(f"set_a: {set_a}")
print(f"set_b: {set_b}")
print(f"set_c: {set_c}")
print(f"universal_set: {universal_set}\n")

# Union operations
print("Union Operations:")
print("Method: set_a.union(set_b) =", set_a.union(set_b))
print("Operator: set_a | set_b =", set_a | set_b, "\n")

# Intersection operations
print("Intersection Operations:")
print("Method: set_a.intersection(set_b) =", set_a.intersection(set_b))
print("Operator: set_a & set_b =", set_a & set_b, "\n")

# Difference operations
print("Difference Operations:")
print("Method: set_a.difference(set_b) =", set_a.difference(set_b))
print("Operator: set_a - set_b =", set_a - set_b, "\n")

# Symmetric Difference operations
# What is this?  Formula and Venn diagram.... (A U B) - (A ^ B)
print("Symmetric Difference Operations:")
print("Method: set_a.symmetric_difference(set_b) =", set_a.symmetric_difference(set_b))
print("Operator: set_a ^ set_b =", set_a ^ set_b, "\n")

# Subset checks
print("Subset Checks:")
print("Method: set_c.issubset(set_a) =", set_c.issubset(set_a))
print("Operator: set_c <= set_a =", set_c <= set_a, "\n")

# Superset checks
print("Superset Checks:")
print("Method: set_a.issuperset(set_c) =", set_a.issuperset(set_c))
print("Operator: set_a >= set_c =", set_a >= set_c, "\n")

# Disjoint check
print("Disjoint Check:")
print("Method: set_a.isdisjoint({7, 8}) =", set_a.isdisjoint({7, 8}), "\n")

# In-place operations
print("In-place Operations:")
set_a_copy = set_a.copy()
set_a_copy.update(set_b)
print("After set_a_copy.update(set_b):", set_a_copy)

set_a_copy = set_a.copy()
set_a_copy |= set_b
print("After set_a_copy |= set_b:", set_a_copy, "\n")

# Complement using difference with universal set
print("Complement Operations:")
print("Complement of set_a in universal_set:", universal_set - set_a, "\n")

# Element operations
print("Element Operations:")
set_a.add(5)
print("After set_a.add(5):", set_a)

set_a.discard(5)
print("After set_a.discard(5):", set_a)

set_a.remove(4)
print("After set_a.remove(4):", set_a)

popped = set_a.pop()
print(f"Popped element: {popped}, Remaining set: {set_a}")

# Membership test
print("\nMembership Tests:")
print("Is 3 in set_a?", 3 in set_a)
print("Is 10 not in set_a?", 10 not in set_a)


# checkpoint questions
# can we write python methods to see whether a collection of sets are mutually exhaustive?
# ...are a partition



"""Basics of importing code from modules and github"""

import random
import numpy as np
import matplotlib.pyplot as plt

#random.randint(1, 100)
#np.zeros(3)
#plt.scatter(np.linspace(0, 100, 1000), np.linspace(0, 100, 1000) + np.random.normal(0, 10, 1000))

"""
note in ipython (jupyter notebooks) "!" escapes to terminal
this command in a jupyter notebook (e.g. Colab) will pull the course code repo
!git clone https://github.com/dougfaust/WWU_Math341.git

Otherwise, run this in a terminal with git cli installed
git clone https://github.com/dougfaust/WWU_Math341.git

Or, navigate to
https://github.com/dougfaust/WWU_Math341
and download what you want 
"""

from WWU_Math341.hw_two_utils import Card, CardDeck
from WWU_Math341.hw_two_utils import plot_convergence_curves
import numpy as np

deck1 = CardDeck()
deck2 = CardDeck()

deck1.__getitem__(9)
