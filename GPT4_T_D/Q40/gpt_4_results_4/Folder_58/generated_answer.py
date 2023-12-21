
def return_n_smallest_chars(s):
    s_list = sorted(s, key=ord)
    return sorted(s_list[:49], reverse=True)
