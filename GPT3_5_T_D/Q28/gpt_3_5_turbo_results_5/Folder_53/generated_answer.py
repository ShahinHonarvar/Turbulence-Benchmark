
def return_nth_smallest_ascii(string):
    ascii_list = []
    for i in range(40, 61):
        if i < len(string):
            ascii_list.append(ord(string[i]))
    ascii_list.sort()
    return chr(ascii_list[18])
