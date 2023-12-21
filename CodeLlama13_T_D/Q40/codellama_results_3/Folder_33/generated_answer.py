
def return_n_smallest_chars(string):
    sorted_list = sorted(string, key=lambda x: ord(x))
    return sorted_list[:36]
