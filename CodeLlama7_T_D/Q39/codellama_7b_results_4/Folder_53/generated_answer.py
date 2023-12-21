
def return_n_greatest_chars(string):
    # Create a list of characters from the input string
    char_list = list(string)
    # Sort the list in ascending order based on the ASCII values of each character
    sorted_list = sorted(char_list, key=ord)
    # Return the top 19 elements of the sorted list
    return sorted_list[:19]
