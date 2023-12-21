
def return_nth_smallest_ascii(string):
    ascii_list = []
    for i in range(5):
        if string[i] not in ascii_list:
            ascii_list.append(ord(string[i]))
    ascii_list.sort()
    return chr(ascii_list[3])
