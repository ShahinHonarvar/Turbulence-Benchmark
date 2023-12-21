
def return_nth_smallest_ascii(s):
    char_list = sorted(list(s[20:81]), key=ord)
    return char_list[10]
