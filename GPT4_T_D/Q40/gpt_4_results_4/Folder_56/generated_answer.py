
def return_n_smallest_chars(s):
    s_list = list(s)
    s_list.sort(key=ord)
    return s_list[:21]
