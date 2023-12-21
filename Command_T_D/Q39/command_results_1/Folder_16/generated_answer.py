import string
def return_n_greatest_chars(s):
    return sorted(set(s), key=lambda x: string. ascii_lowercase.index(x))[:64]
