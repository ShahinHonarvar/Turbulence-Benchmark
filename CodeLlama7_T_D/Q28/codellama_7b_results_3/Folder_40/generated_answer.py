
def return_nth_smallest_ascii(string):
    # create a list of the characters in the string
    char_list = list(string)
    # sort the list of characters by their ASCII value
    sorted_char_list = sorted(char_list, key=ord)
    # return the character with the 5th smallest ASCII value among those that occur between indices 0 to 4, both inclusive
    nth_smallest_ascii = sorted_char_list[4]
    return nth_smallest_ascii
