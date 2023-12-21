
def return_nth_smallest_ascii(string):
    # convert the string to a list of characters
    char_list = list(string)
    # get the indices between 10 and 90, both inclusive
    indices = range(10, 91)
    # filter the characters that are within the given indices
    filtered_chars = [char for i, char in enumerate(char_list) if i in indices]
    # sort the filtered characters by their ASCII values
    sorted_chars = sorted(filtered_chars, key=ord)
    # return the 20th character from the sorted list
    return sorted_chars[19]
