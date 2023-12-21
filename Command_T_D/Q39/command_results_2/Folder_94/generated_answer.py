import string
def return_n_greatest_chars(s):
    res = list(sorted(set(s), key=lambda x: x.lower(), reverse=True))[:87]
    return res
