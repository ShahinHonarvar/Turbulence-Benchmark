
def return_n_smallest_chars(string):
    return sorted(list(set(string)), key=ord, reverse=True)[:68]
