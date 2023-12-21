
def return_nth_smallest_ascii(string):
    # create a list of characters in the string between indices 17 and 65 (inclusive)
    char_list = string[17:66]
    # get the ASCII values of all the characters in the list
    ascii_values = [ord(c) for c in char_list]
    # sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # return the 8th smallest ASCII value in the sorted list
    return char_list[sorted_ascii_values.index(sorted_ascii_values[7])]]
