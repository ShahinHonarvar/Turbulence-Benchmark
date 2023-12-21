
def return_n_greatest_chars(string):
    return sorted(set(string), key=ord, reverse=True)[:16]
