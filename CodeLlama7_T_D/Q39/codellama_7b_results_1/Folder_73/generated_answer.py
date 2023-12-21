
def return_n_greatest_chars(my_string, n):
    # Convert the string to a list of characters
    char_list = list(my_string)
    # Sort the list of characters by their ASCII values in descending order
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top n elements of the sorted list
    return sorted_list[:n]
