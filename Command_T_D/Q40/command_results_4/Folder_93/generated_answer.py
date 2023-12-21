import sys
def return_n_smallest_chars(s):
    return sorted(s, key=lambda c:(c.lower(), ord(c)), reverse=True)[:77]
