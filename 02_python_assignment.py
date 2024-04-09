from hw_two_utils import Card, CardDeck
from hw_two_utils import plot_convergence_curves
import numpy as np

if __name__ == "__main__":

    #####
    # play around with the Card and CardDeck classes
    #####
    random_card = Card('4', 'Clubs')
    print(random_card)

    crazy_new_card = Card('23', 'Horseshoes')
    print(crazy_new_card)

    unshuffled = CardDeck()
    print(unshuffled[1])
    print(unshuffled[3:6])

    #####
    # print output from your four functions for a large number of trials
    #####


    #####
    # visualize how your experiments converge here using the provided plot_convergence_curves method
    #####
    def example_prob_func(t):
        return sum(np.random.binomial(t, 0.7, 1))/t

    plot_convergence_curves(example_prob_func, 1000)

