import sys
def return_n_greatest_chars(s):
    return [c for c in sorted(s)[::-1][:21]]
