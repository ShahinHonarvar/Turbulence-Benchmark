
def return_n_greatest_chars(my_string):
    # Split the string into a list of characters
    char_list = list(my_string)
    # Sort the list in ascending order based on the ASCII values of each character
    sorted_list = sorted(char_list, key=ord)
    # Return the top 73 characters from the sorted list
    return sorted_list[:73]
