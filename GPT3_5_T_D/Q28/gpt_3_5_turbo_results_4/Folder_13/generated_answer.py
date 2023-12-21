
def return_nth_smallest_ascii(string):
    substring = string[47:81]
    char_list = list(substring)
    char_list.sort()
    return char_list[3]
