
def return_nth_smallest_ascii(string):
    # convert the string to a list of characters
    char_list = list(string)
    # create a dictionary to keep track of the ASCII values
    ascii_dict = {}
    # loop through the characters in the string
    for char in char_list:
        # if the character is not already in the dictionary
        if char not in ascii_dict:
            # add the character to the dictionary and set its value to 1
            ascii_dict[char] = 1
        else:
            # if the character is already in the dictionary, increment its value by 1
            ascii_dict[char] += 1
    # sort the dictionary by key (character)
    sorted_dict = sorted(ascii_dict.items(), key=lambda x: x[0])
    # get the character with the 15th smallest ASCII value
    nth_smallest_char = sorted_dict[14][0]
    return nth_smallest_char
