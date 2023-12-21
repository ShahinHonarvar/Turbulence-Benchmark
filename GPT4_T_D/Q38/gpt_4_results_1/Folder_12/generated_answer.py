
from itertools import combinations

def find_subset_of_length_n(element_set):
  subsets = list(combinations(element_set, 27))
  return len(subsets)
