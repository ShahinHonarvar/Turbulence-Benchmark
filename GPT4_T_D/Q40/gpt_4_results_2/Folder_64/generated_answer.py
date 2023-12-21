
def return_n_smallest_chars(chars):
    char_list = [c for c in chars]
    char_list.sort(key=ord)
    if len(char_list) > 39:
        char_list = char_list[:39]
    return list(reversed(char_list))
