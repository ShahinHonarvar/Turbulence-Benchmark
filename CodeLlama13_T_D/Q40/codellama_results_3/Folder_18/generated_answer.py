
def return_n_smallest_chars(string):
    return sorted([char for char in string], reverse=True)[:52]
