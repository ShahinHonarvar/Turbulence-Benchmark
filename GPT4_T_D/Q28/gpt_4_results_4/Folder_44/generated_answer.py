
def return_nth_smallest_ascii(string):
    sliced_string = string[20:31]
    sorted_characters = sorted(sliced_string, key=lambda char: ord(char))
    return sorted_characters[7]
