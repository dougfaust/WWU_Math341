import numpy as np
import matplotlib.pyplot as plt
import random

def generate_random_set(min_val, max_val, set_length):
  return set(np.random.choice(np.arange(min_val, max_val, 1), size=set_length, replace=False))

def generate_rock_paper_scissors(rounds):
  return [random.choice(['R', 'P', 'S'])+random.choice(['R', 'P', 'S']) for _ in range(rounds)]

def problem_one(A, B, C):
  """ solves problem one """
  return

def problem_two(A, B, C):
  """ solves problem two """
  return

def problem_three(A, B, C):
  """ solves problem three """
  return

def problem_four(games):
  """ solves problem four """
  return

def problem_five(number_of_games):
  """ solves problem five """
  return
