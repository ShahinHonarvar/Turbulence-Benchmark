
def return_n_greatest_chars(string):
    return sorted([char for char in set(string)], key=ord)[:21]
