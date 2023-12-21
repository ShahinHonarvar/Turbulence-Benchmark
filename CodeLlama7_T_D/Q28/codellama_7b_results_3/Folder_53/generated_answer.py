
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the indices of the characters that occur between indices 40 and 60 (both inclusive)
    start_index = 40
    end_index = 60
    char_indices = [i for i, x in enumerate(char_list) if start_index <= i <= end_index]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list[start_index:end_index+1]), key=ord)
    # Return the character with the 19th smallest ASCII value among those characters in the string that occur between indices 40 to 60, both inclusive.
    return sorted_chars[19]
