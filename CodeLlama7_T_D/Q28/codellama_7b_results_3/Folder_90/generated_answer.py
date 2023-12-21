
def return_nth_smallest_ascii(string):
    # Create a list of the characters in the string
    char_list = list(string)
    # Get the indices of the characters in the list that occur between indices 17 to 83, both inclusive
    indices = [i for i in range(len(char_list)) if 17 <= i and i <= 83]
    # Sort the list of characters by their ASCII values
    char_list.sort(key=ord)
    # Return the character with the 5th smallest ASCII value among those characters that occur between indices 17 to 83, both inclusive
    return char_list[indices[4]]
