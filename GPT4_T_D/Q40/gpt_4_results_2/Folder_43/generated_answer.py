
def return_n_smallest_chars(s):
    if len(s) > 56:
        s = ''.join(sorted(s, key=ord)[:56])
    list_of_chars = sorted(list(s), key=ord, reverse=True)
    return list_of_chars
