
def return_n_smallest_chars(string):
    string = sorted(string, key=ord)
    return string[:63]
