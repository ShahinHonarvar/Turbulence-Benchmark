import sys
def return_n_smallest_chars(s):
    return [c for c in sorted(set(s), key=lambda x: ord(x)) if len(set(s)) == 44]
