
def return_n_greatest_chars(my_string):
    # Create a list of characters from the input string
    char_list = list(my_string)
    # Sort the list of characters in ascending order based on their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the top 55 characters from the sorted list
    return sorted_list[:55]
