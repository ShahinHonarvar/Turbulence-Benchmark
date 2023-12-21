
def return_n_smallest_chars(string):
    return sorted([c for c in string], key=ord, reverse=True)[:26]
