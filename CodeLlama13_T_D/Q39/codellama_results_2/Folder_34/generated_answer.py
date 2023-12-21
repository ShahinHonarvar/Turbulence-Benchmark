
def return_n_greatest_chars(s):
    chars = sorted([c for c in s], key=ord, reverse=True)[:9]
    return ''.join(chars)
