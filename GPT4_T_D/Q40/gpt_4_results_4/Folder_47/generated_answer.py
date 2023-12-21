
def return_n_smallest_chars(string):
    list_chars = sorted(string, key=ord)[:21]
    list_chars.sort(reverse=True)
    return list_chars
