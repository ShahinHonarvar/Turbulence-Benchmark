import sys
import math
def find_subset_of_length_n(s):
    if not s:
        return 1
    if len(s) == 1:
        return 1
    if len(s) == 2:
        return 2
    return math.factorial(len(s)) / math.factorial(s)
