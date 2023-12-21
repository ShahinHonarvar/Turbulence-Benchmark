
def return_n_greatest_chars(string):
    return sorted([c for c in set(string)], key=ord, reverse=True)[:11]
