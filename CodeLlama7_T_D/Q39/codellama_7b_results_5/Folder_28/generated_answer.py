
def return_n_greatest_chars(my_string):
    # Split the string into a list of characters
    char_list = list(my_string)
    # Sort the list of characters by ASCII value in descending order
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 3 characters with the greatest ASCII values
    return sorted_char_list[:3]
