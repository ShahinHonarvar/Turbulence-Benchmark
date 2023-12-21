import string
def return_n_greatest_chars(s):
    return list(sorted(s, key=lambda x: string.ascii_letters.index(x), reverse=True))
