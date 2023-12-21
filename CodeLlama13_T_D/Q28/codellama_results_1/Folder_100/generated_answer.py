
def return_nth_smallest_ascii(string):
    char_list = []
    for i in range(5, 48):
        if string[i] not in char_list:
            char_list.append(string[i])
    ascii_values = [ord(c) for c in char_list]
    nth_smallest = sorted(ascii_values)[12]
    return chr(nth_smallest)
