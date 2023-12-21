
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=ord)
    smallest_chars = sorted_string[:49]
    smallest_chars.sort(reverse=True)
    return smallest_chars
