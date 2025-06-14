
def return_n_greatest_chars(string, n):
    # Sort the characters in the string based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return the top n characters from the sorted list
    return sorted_chars[-n:]
