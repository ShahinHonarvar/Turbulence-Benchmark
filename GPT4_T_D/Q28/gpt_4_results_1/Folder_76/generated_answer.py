
def return_nth_smallest_ascii(s):
    char_list = list(s[18:67])
    char_list.sort(key=ord)
    return char_list[18]
