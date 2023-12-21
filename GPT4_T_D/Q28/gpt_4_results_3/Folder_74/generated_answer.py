
def return_nth_smallest_ascii(s):
    char_list = list(set(s[1:32]))
    sorted_chars = sorted(char_list, key=ord)
    return sorted_chars[5]
