
def return_nth_smallest_ascii(input_string):
    char_list = list(set(input_string[8:27]))
    char_list.sort(key=ord)
    return char_list[5]
