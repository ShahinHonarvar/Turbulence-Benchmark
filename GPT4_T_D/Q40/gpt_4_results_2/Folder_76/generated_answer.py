
def return_n_smallest_chars(s):
    char_list = list(s)
    char_list.sort(key=ord)
    smallest_3_chars = char_list[:3]
    smallest_3_chars.sort(reverse=True)
    return smallest_3_chars
