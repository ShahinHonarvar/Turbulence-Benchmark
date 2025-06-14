
def return_nth_smallest_ascii(string):
    # create a list of characters in the string
    char_list = list(string)
    # get the ASCII values of each character
    ascii_values = [ord(char) for char in char_list]
    # sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # return the 5th smallest ASCII value
    return chr(sorted_ascii_values[4])
