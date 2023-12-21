
def return_n_smallest_chars(string):
    string = sorted([char for char in set(string)], key=ord)[:26]
    return string[::-1]
