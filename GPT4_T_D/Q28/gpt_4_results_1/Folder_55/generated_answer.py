
def return_nth_smallest_ascii(s):
    char_list = list(s[:13])
    char_list.sort(key=lambda x: ord(x))
    return char_list[12]
