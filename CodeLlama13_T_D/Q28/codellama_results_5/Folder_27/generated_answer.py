
def return_nth_smallest_ascii(string):
    ascii_list = list()
    for i in range(33, 86):
        if string[i] not in ascii_list:
            ascii_list.append(string[i])
    
    return sorted(ascii_list)[12]
