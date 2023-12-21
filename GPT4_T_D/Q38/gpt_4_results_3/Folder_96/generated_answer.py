
import math

def find_subset_of_length_n(s):
    n = len(s)
    if n < 47:
        return 0
    else:
        return math.factorial(n) / (math.factorial(47) * math.factorial(n - 47))
