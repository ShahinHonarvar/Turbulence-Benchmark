
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=ord, reverse=True)
    return sorted_string[:75]
