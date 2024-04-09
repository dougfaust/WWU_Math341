import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class CardDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


class HyperCardDeck:
    # code here

    def __init__(self):
        # code here
        pass

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

def problem_one(n_cards):
    """ instantiate a card deck, shuffle, and return the first n_cards """
    return

def problem_two(trials):
    """" estimate the probability of two of a kind in straight 5-card poker """
    return

def problem_three(trials):
    """ estimate the probability of a flush in straight 5-card poker """
    return

def problem_four(trials):
    """ estimate the probability of two of a kind in straight 5-card hyperpoker """
    return

def problem_five(trials):
    """ estimate the probability of a flush in straight 5-card hyperpoker """

def plot_convergence_curves(probability_estimating_function, max_trials):
    ds = min(max_trials, 200)
    df = pd.DataFrame(np.linspace(1, max_trials, ds), columns=['trials'])

    for c in ['run_' + str(i+1) for i in range(6)]:
        df[c] = df['trials'].apply(probability_estimating_function)

    df.set_index(['trials'], inplace=True)
    df.plot(ylabel='N_events \ N', title='Estimated Probability After Number of Trials')
    plt.show()
    return True
