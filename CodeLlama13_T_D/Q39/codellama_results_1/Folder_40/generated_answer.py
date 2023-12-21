
def return_n_greatest_chars(string):
    # Create a list of tuples containing the character and its ASCII value
    char_ascii = [(char, ord(char)) for char in string]
    
    # Sort the list by the second element (ASCII value) in descending order
    sorted_chars = sorted(char_ascii, key=lambda x: -x[1])
    
    # Return a list of the first 7 characters with the greatest ASCII values
    return [char for char, _ in sorted_chars[:7]]
