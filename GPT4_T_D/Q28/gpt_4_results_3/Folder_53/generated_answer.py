
def return_nth_smallest_ascii(string):
    string = string[40:61]
    sorted_chars = sorted([char for char in string], key = ord)
    return sorted_chars[18]
