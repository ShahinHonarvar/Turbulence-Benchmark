import sys
def find_subset_of_length_n(s):
    return sys.set_recursion_limit(10**5) # 10**5 is a good number.
    return s.count(1) * 2 ** (len(s) - 1) # This is the formula.
