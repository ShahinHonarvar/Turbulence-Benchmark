
def return_nth_smallest_ascii(input_string):
    ascii_characters = [char for char in input_string[0:6]]
    ascii_characters.sort(key=ord)
    return ascii_characters[5]
