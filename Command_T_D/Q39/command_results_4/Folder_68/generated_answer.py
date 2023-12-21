import string
def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: string.ascii_lowercase.index(x))[:89]
