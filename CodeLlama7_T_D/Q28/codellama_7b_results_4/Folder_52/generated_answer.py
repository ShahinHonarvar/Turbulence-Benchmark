
def return_nth_smallest_ascii(string):
    # create a list of all characters in the string
    char_list = list(string)

    # find the indices of the characters that occur between 46 and 72
    start_index = char_list.index('{')
    end_index = char_list.index('}')

    # create a list of all characters between the start and end indices
    char_range = char_list[start_index:end_index]

    # find the character with the 15th smallest ASCII value in the range
    ascii_values = [ord(char) for char in char_range]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii_value = sorted_ascii_values[14]

    # return the character with that ASCII value
    return chr(nth_smallest_ascii_value)
