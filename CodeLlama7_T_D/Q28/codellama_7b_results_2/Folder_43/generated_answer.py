
def return_nth_smallest_ascii(s):
    # find the indices of the characters in the string that occur between indices 14 to 35, both inclusive
    start_index = s.find(chr(14))
    end_index = s.find(chr(36))
    # get a list of all the characters in the string that occur between these indices
    char_list = []
    for i in range(start_index, end_index + 1):
        char_list.append(s[i])
    # sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # return the 11th smallest ASCII value among these characters
    return sorted_list[10]
