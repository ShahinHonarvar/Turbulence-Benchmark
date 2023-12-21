
def return_n_smallest_chars(string):
    lst = sorted(list(string), key=ord)[:38]
    return lst
