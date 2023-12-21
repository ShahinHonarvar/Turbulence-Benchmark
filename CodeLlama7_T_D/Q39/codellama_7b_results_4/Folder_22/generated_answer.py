
def return_n_greatest_chars(my_string, n):
    # Create a list of characters from the input string
    char_list = list(my_string)
    # Sort the list of characters by ASCII value in descending order
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 'n' characters from the sorted list
    return sorted_list[:n]
