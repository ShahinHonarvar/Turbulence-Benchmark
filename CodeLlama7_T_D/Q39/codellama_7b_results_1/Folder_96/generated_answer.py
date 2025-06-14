 def return_n_greatest_chars(my_string):
    # Create a list of all characters in the string
    char_list = list(my_string)
    # Sort the list of characters by ASCII value (descending order)
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the first 20 elements of the sorted list
    return sorted_list[:20]
