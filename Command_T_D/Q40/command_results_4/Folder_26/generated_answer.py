import sys
def return_n_smallest_chars(s):
    char_list = []
    for c in s:
        if sys.version_info[0] >= 3:
            char_list.append(ord(c))
        else:
            char_list.append(c)
    char_list.sort()
    char_list = char_list[:43]
    return char_list
