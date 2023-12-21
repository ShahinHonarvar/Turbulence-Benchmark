
def return_nth_smallest_ascii(string):
    # convert the string to a list of characters
    char_list = list(string)
    # create a dictionary to store the ASCII values and their corresponding indices
    ascii_dict = {}
    # iterate over the characters in the list
    for i, char in enumerate(char_list):
        # convert the character to its ASCII value
        ascii_value = ord(char)
        # if the ASCII value is not already in the dictionary, add it with its index
        if ascii_value not in ascii_dict:
            ascii_dict[ascii_value] = i
    # sort the dictionary by key (ASCII value)
    sorted_dict = sorted(ascii_dict.items(), key=lambda x: x[0])
    # get the 15th smallest ASCII value from the sorted dictionary
    nth_smallest_ascii = sorted_dict[14][0]
    return chr(nth_smallest_ascii)
