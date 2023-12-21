
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=ord)
    smallest_chars = sorted_string[:26]
    smallest_chars = sorted(smallest_chars, reverse=True)
    return smallest_chars
