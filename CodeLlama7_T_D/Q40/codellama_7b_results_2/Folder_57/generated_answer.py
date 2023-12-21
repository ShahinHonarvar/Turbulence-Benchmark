
def return_n_smallest_chars(input_string):
    # convert input string to a list of characters
    char_list = list(input_string)
    # sort the list of characters in descending order based on ASCII values
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # return the top 29 characters from the sorted list
    return sorted_char_list[:29]
