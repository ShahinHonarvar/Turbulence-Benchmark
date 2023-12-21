 def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Get the indices of the characters that occur between indices 33 and 85, both inclusive
    indices = [i for i, c in enumerate(char_list) if 33 <= i <= 85]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Get the 13th smallest ASCII value among the characters that occur between indices 33 and 85, both inclusive
    nth_smallest = sorted_chars[indices[12]]
    return nth_smallest
