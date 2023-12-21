
def return_n_smallest_chars(string):
    lst = sorted(string, key=ord)[:11]
    return lst[::-1]
