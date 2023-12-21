
def return_nth_smallest_ascii(string):
    sublist = string[51:61]
    ascii_list = [ord(c) for c in sublist]
    ascii_list.sort()
    return chr(ascii_list[4])
