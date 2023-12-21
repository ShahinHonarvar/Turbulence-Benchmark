
def return_n_smallest_chars(string):
    list_chars = list(string)
    sorted_list = sorted(list_chars, key=lambda x: ord(x))
    return sorted_list[:72]
