
def return_n_greatest_chars(my_string):
    # Create a list of all the characters in the string
    char_list = list(my_string)
    # Sort the list in descending order based on the ASCII value of each character
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 38 characters from the sorted list
    return sorted_list[:38]
