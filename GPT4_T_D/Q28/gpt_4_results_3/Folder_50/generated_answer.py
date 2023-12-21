
def return_nth_smallest_ascii(input_string):
    char_list = list(set(input_string[25:89]))
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    return sorted_chars[10]
