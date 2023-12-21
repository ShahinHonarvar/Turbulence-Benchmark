
def return_nth_smallest_ascii(string):
    # Extract the substring of interest
    substr = string[52:79+1]
    # Create a list of all characters in the substring
    char_list = list(substr)

    # Sort the list of characters by their ASCII values
    char_list.sort(key=ord)

    # Return the 7th smallest ASCII value
    return char_list[6]
