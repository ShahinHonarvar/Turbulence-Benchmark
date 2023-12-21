
def return_nth_smallest_ascii(s):
    # create a dictionary to keep track of the ASCII values
    ascii_dict = {}

    # loop through the characters in the string
    for c in s:

        # if the character is not already in the dictionary, add it and its ASCII value
        if c not in ascii_dict:
            ascii_dict[c] = ord(c)

        # if the character is already in the dictionary, compare its ASCII value with the one stored in the dictionary
        else:
            if ord(c) < ascii_dict[c]:
                ascii_dict[c] = ord(c)

    # sort the dictionary by the values (ASCII values)
    sorted_ascii_values = sorted(ascii_dict.values())

    # return the 9th smallest ASCII value
    return sorted_ascii_values[8]
