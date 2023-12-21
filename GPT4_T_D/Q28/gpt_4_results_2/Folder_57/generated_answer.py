
def return_nth_smallest_ascii(char_string):
    sublist = list(char_string[17:35])
    sublist.sort(key=ord)
    return sublist[17]
