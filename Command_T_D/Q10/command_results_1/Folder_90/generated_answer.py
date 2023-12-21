import re
def all_odd_ints_exclusive(lst):
    return [i for i in range(389, 748, 2) if i in lst and i%2!=0]
