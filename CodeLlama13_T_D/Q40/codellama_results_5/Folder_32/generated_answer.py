
def return_n_smallest_chars(string):
    sorted_list = sorted(string, key=lambda x: ord(x))[:8]
    return sorted_list
