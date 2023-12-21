import sys
def return_n_greatest_chars(s):
    return [i for i in sorted(set(s), key=lambda x: -x.lower())][:90]
