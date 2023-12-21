
def return_n_smallest_chars(string):
    char_list = []
    for i in range(12):
        smallest_char = ""
        smallest_value = 256
        for char in string:
            if ord(char) < smallest_value:
                smallest_value = ord(char)
                smallest_char = char
        char_list.append(smallest_char)
    return sorted(char_list)
