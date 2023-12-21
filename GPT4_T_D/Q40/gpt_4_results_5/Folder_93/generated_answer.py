
def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=lambda x: ord(x))
    s_list = sorted_s[:77]
    s_list.sort(reverse=True)
    return s_list
