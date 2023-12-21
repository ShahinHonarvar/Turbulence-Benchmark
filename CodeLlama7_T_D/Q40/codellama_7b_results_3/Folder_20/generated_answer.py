
def return_n_smallest_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Sort the list in ascending order based on the ASCII value of each character
    char_list.sort(key=ord)
    # Return the first 40 characters of the sorted list
    return char_list[:40]
