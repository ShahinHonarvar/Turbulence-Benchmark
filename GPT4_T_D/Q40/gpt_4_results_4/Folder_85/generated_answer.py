
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=ord)
    smallest_chars = sorted_string[:85]
    smallest_chars.reverse()
    return smallest_chars
