import sys
def return_n_smallest_chars(s):
    return [x for x in sorted(s, key=lambda x: ord(x))][:17]
