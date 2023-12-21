
def return_nth_smallest_ascii(string):
    # create a list of the characters in the string that occur between indices 33 and 85
    char_list = [char for char in string if 33 <= ord(char) <= 85]
    # sort the list by ASCII value
    sorted_list = sorted(char_list, key=ord)
    # return the character with the 13th smallest ASCII value
    return sorted_list[12]
