
def return_n_smallest_chars(string):
    return sorted([char for char in string], key=ord, reverse=True)[:72]
