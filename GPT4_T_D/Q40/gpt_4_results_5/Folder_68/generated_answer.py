
def return_n_smallest_chars(string):
    chars_list = sorted(string, key=ord)[:89]
    chars_list.sort(reverse=True)
    return chars_list
