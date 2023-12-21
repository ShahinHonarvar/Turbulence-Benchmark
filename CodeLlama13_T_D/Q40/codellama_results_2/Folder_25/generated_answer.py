
def return_n_smallest_chars(string):
    char_list = []
    for i in range(29):
        min_value = float('inf')
        min_char = ''
        for char in string:
            if ord(char) < min_value and char not in char_list:
                min_value = ord(char)
                min_char = char
        char_list.append(min_char)
    return sorted(char_list)
