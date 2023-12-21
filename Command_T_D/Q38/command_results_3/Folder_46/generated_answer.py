import math
def find_subset_of_length_n(s):
    return math.factorial(len(s)) // math.factorial(len(s)-14)
