
import itertools

def find_subset_of_length_n(s):
    if len(s) < 27:
        return 0
    else:
        return len(list(itertools.combinations(s, 27)))
