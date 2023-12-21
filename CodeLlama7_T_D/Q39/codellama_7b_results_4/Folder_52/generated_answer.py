
def return_n_greatest_chars(string, n=68):
    # Convert the string to a list of characters
    char_list = list(string)
    # Sort the list of characters by ASCII value in descending order
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top n characters from the sorted list
    return sorted_list[:n]
