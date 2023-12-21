
def return_n_greatest_chars(input_string, n=10):
    # convert the input string to a list of characters
    char_list = list(input_string)

    # sort the list of characters by ASCII value in descending order
    sorted_char_list = sorted(char_list, key=ord, reverse=True)

    # return the top n characters from the sorted list
    return sorted_char_list[:n]
