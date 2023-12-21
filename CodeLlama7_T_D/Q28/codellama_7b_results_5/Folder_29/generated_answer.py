
def return_nth_smallest_ascii(string):
    # convert the string to a list of characters
    char_list = list(string)
    # sort the list of characters based on their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # return the 6th smallest ASCII value among those characters in the string that occur between indices 5 to 10, both inclusive.
    return sorted_list[5:10+1][5]]
