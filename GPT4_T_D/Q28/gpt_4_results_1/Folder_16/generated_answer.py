
def return_nth_smallest_ascii(s):
    char_list = list(set(s[18:46]))
    char_list.sort(key=ord)
    return char_list[6]
