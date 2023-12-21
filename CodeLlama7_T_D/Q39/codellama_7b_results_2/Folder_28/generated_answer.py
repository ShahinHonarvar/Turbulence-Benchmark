
def return_n_greatest_chars(string, n=3):
    # Convert the string to a list of characters
    char_list = list(string)
    # Sort the list of characters by ASCII value in descending order
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # Return the first n elements of the sorted list
    return sorted_char_list[:n]
