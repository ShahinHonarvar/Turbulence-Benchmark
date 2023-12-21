
def return_nth_smallest_ascii(str_arg):
    char_list = list(set(str_arg[1:67]))
    char_list.sort(key=ord)
    return char_list[7]
