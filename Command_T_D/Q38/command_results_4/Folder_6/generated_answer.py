import math
def find_subset_of_length_n(set):
    # calculate the total number of possible subsets of size 89
    # by calculating the number of permutations of the set
    # taking into account the number of possible ways to
    # select 89 elements from a set of size N
    return math.factorial(len(set)) / math.factorial(89) / math.factorial(len(set)-89)
