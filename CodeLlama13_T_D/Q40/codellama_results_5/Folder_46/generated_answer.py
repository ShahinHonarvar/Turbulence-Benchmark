
def return_n_smallest_chars(string):
    sorted_list = sorted(string, key=ord)[:54]
    return sorted_list[::-1]
