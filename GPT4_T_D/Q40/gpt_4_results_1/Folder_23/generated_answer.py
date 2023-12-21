
def return_n_smallest_chars(string):
    string_list = list(string)
    string_list.sort(key=ord)
    return string_list[:46]
