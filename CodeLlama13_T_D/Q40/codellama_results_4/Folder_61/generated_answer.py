
def return_n_smallest_chars(s):
    char_list = []
    for i in s:
        if len(char_list) < 66:
            char_list.append(i)
        else:
            break

    return sorted(char_list, reverse=True)
