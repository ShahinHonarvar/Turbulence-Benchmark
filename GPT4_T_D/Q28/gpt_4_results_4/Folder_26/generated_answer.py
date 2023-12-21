
def return_nth_smallest_ascii(s):
    char_list = sorted(s[1:37], key=ord)
    return char_list[14]
