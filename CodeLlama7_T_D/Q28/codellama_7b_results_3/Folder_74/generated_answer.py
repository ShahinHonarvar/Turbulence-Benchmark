
def return_nth_smallest_ascii(string):
    # create a list of all the characters in the string
    char_list = []
    for char in string:
        if char not in char_list:
            char_list.append(char)
    # sort the list of characters by their ASCII value
    sorted_list = sorted(char_list, key=ord)
    # return the 6th smallest ASCII value
    return sorted_list[5]
