
def return_n_greatest_chars(string):
    # Convert the string to a list of characters
    char_list = list(string)

    # Sort the list of characters by ASCII value in descending order
    sorted_char_list = sorted(char_list, key=ord, reverse=True)

    # Return the first 37 elements of the sorted list
    return sorted_char_list[:37]
