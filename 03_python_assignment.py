"""
MATH 341 programming assignment 3
Student:
"""

import pandas as pd

def problem_one(url = None):
    """load csv from url and return dataframe with new Position_type column"""
    return

def problem_two(df, category, N=5):
    """Write a method to return the top N players in some numerical category contained within df.columns"""
    top_players_list = []
    return top_players_list

def problem_three(df, n_goals=10, position='C'):
    """conditional probability problem: probability that a player scores > n_goals goals | C, W, D"""
    if position not in ('C', 'W', 'D'):
        raise ValueError(f"{position} is an invalid position, choose from 'C', 'W', 'D'")

    return

def problem_four(df):
    """Bayes theorem problem: probability that player is C, W, D given they score > 10 goals"""
    print("Just report the answers you calculate using print statements")
    return

def problem_five(df):
    """all-star team: clearly state criteria / external data for EC"""
    return

if __name__ == "__main__":

    # example syntax
    NHL_df = problem_one('https://raw.csvfile.com/location/file.csv')

    top_ten_points = problem_two(NHL_df, 'Pts', 10)

    n_goals = 10
    for pos in ['C', 'W', 'D', 'Zamboni_Driver']:
        probability = problem_three(NHL_df, n_goals, pos)
        print(f"P(scoring {n_goals} goals | {pos}) = {probability}")

    problem_four(NHL_df)

    all_star_team = problem_five(NHL_df)