
def return_n_smallest_chars(s):
    s_sort = sorted(s, key=lambda x: ord(x))
    if len(s_sort) > 44:
        s_sort = s_sort[:44]
    s_sort.reverse()
    return s_sort
