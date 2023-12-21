
def return_n_greatest_chars(s):
    return sorted(s, reverse=True, key=lambda c: ord(c))[:46]
