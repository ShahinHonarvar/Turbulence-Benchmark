
def return_n_greatest_chars(s):
    return sorted(set(s), key=ord, reverse=True)[:64]
