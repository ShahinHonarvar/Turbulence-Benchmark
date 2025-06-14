
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Get the indices of the characters in the list that occur between indices 25 and 64, both inclusive
    indices = [i for i in range(len(char_list)) if 25 <= i <= 64]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Return the character with the 6th smallest ASCII value among those characters in the list that occur between indices 25 and 64, both inclusive.
    return sorted_chars[indices[5]]
