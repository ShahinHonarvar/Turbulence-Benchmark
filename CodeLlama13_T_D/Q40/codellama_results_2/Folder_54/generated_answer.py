
def return_n_smallest_chars(string):
    chars = sorted([c for c in string if c.isalnum()], key=ord)
    return chars[:79]
