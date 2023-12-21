
def return_n_smallest_chars(s):
    char_list = sorted(s, key=ord)
    smallest_chars = char_list[:29]
    smallest_chars.sort(reverse=True)
    return smallest_chars
