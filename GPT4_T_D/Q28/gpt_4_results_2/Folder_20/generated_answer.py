
def return_nth_smallest_ascii(s):
    char_list = list(s[25:65])
    char_list.sort(key=ord)
    return char_list[5]
