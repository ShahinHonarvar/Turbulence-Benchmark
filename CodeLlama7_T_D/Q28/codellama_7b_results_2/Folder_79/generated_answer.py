
def return_nth_smallest_ascii(string):
    # create a dictionary to store the character and its ASCII value
    ascii_dict = {}

    # loop through each character in the string

    for char in string:

        # if the character is already in the dictionary, skip it

        if char in ascii_dict:
            continue

        # otherwise, add the character and its ASCII value to the dictionary

        else:
            ascii_dict[char] = ord(char)

    # sort the dictionary by the ASCII value of each character

    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[1])

    # return the 18th smallest ASCII value in the sorted dictionary

    return sorted_ascii_dict[17][0]
