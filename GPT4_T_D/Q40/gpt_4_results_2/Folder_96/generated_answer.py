
def return_n_smallest_chars(string):
    ascii_list = [char for char in string]
    ascii_list.sort(key=ord)
    smallest_chars = ascii_list[:20]
    smallest_chars.sort(reverse=True)
    return smallest_chars
