
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the indices of the characters in the list that occur between indices 58 to 85, both inclusive
    indices = [i for i, x in enumerate(char_list) if 58 <= i <= 85]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Return the character with the 19th smallest ASCII value among those characters that occur between indices 58 to 85, both inclusive
    return sorted_chars[indices][18]
