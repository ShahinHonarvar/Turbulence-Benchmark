
def return_n_smallest_chars(s):
    char_list = []
    for c in s:
        if len(char_list) < 90 and c not in char_list:
            char_list.append(c)
    sorted_list = sorted(char_list, key=ord)
    return sorted_list[::-1]
