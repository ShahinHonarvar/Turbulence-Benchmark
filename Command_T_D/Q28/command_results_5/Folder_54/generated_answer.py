
def return_nth_smallest_ascii(s):
    ascii_dict = {}
    for i in range(len(s) - 12):
        ascii_dict[s[i]] = ord(s[i])
    ascii_list = sorted(list(ascii_dict.values()))
    return s[12:87][16]
