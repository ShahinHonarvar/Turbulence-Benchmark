
def return_nth_smallest_ascii(string):
    # convert the string to a list of characters
    char_list = list(string)
    # create a dictionary to store the ASCII values and their frequencies
    ascii_dict = {}

    # loop through the characters in the list
    for char in char_list:
        # if the character is not in the dictionary, add it with a frequency of 1
        if char not in ascii_dict:
            ascii_dict[char] = 1

        # otherwise, increment the frequency by 1
        else:
            ascii_dict[char] += 1

    # sort the dictionary by value (frequency)
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[1])

    # get the nth element in the sorted dictionary (based on frequency)
    nth_element = sorted_ascii_dict[5]

    # return the character with the 6th smallest ASCII value
    return nth_element[0]
