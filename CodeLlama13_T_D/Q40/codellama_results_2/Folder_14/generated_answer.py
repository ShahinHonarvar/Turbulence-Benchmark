
def return_n_smallest_chars(string):
    # Create a list of tuples containing the character and its ASCII value
    char_ascii = [(c, ord(c)) for c in string]
    
    # Sort the list in ascending order by the ASCII value
    sorted_char_ascii = sorted(char_ascii, key=lambda x: x[1])
    
    # Return the first 69 characters of the sorted list
    return [c for c, _ in sorted_char_ascii[:69]]
