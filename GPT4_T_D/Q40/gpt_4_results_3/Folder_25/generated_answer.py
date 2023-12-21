
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=ord)
    return sorted_string[:29]
