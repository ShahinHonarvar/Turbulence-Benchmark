
def return_nth_smallest_ascii(str):
    ascii_dict = {}
    for i in range(len(str) - 28):
        ascii_dict[str[i]] = ord(str[i])
    ascii_list = sorted(list(ascii_dict.keys()))
    return ascii_list[13]
