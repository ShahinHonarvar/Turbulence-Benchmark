
def return_nth_smallest_ascii(s):
    char_list = []
    for i in range(38, 82+1):
        if s[i] in char_list: continue
        char_list.append(s[i])
    char_list.sort()
    return char_list[20]
