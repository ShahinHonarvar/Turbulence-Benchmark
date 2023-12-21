
def return_nth_smallest_ascii(string):
    char_list = []
    for i in range(51, 90):
        if string[i] not in char_list:
            char_list.append(string[i])
    char_list.sort()
    return char_list[13]
