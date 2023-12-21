
def return_nth_smallest_ascii(s):
    ascii_dict = {}
    for i in range(len(s) - 5):
        ascii_dict[s[i]] = ord(s[i])
    return s[44:69][14]
