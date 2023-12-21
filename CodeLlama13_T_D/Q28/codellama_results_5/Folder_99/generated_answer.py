
def return_nth_smallest_ascii(string):
    ascii_list = []
    for i in range(17, 65+1):
        if string[i-1].isalpha():
            ascii_list.append(ord(string[i-1]))
    return chr(sorted(ascii_list)[7])
