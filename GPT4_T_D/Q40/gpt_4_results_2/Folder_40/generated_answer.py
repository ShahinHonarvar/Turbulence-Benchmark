
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=ord)[:7]
    return sorted_string[::-1]
