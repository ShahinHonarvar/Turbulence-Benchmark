
def return_nth_smallest_ascii(string):
    # convert the string to a list of characters
    char_list = list(string)
    # get the indices of the characters that occur between 33 and 85
    indices = [i for i, x in enumerate(char_list) if 33 <= ord(x) <= 85]
    # sort the indices by the corresponding ASCII values
    sorted_indices = sorted(indices, key=lambda x: ord(char_list[x]))
    # return the character with the 13th smallest ASCII value among those characters
    return char_list[sorted_indices[12]]
