
import itertools

def find_subset_of_length_n(myset):
    return len(list(itertools.combinations(myset, 15)))
