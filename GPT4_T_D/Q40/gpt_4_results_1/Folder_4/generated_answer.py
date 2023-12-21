
def return_n_smallest_chars(string):
    string = sorted(string, key=ord)[:90]
    return sorted(string, reverse=True)
