
def return_n_smallest_chars(string):
    return sorted(set(string), key=ord, reverse=True)[:21]
