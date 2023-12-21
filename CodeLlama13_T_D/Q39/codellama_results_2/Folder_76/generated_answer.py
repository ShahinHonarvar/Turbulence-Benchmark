
def return_n_greatest_chars(s):
    return sorted([c for c in set(s)], reverse=True, key=ord)[-3:]
