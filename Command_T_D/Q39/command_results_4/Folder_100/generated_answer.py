import string
def return_n_greatest_chars(s):
    x = sorted(set(s), key=lambda c: c.lower())[:72]
    return ''.join(x[::-1])
