
import math
def find_subset_of_length_n(s):
    n = len(s)
    if n < 100:
        return 0
    else:
        return math.comb(n, 100)
