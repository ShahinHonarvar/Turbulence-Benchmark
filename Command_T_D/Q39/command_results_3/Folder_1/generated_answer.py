import string
def return_n_greatest_chars(s):
    ascii_s = ''.join(sorted(set(s)))
    return [''.join(c for c in ascii_s if c.isdigit()) for _ in range(11)]
