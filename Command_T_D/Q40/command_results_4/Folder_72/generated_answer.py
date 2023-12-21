import sys
def return_n_smallest_chars(s):
    return sorted(set(s), key=lambda c: ord(c), reverse=True)[:37]
