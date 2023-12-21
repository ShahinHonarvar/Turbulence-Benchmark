
def return_n_smallest_chars(string):
    # Create a list of tuples where each tuple contains a character and its ASCII value
    char_ascii = [(char, ord(char)) for char in string]
    
    # Sort the list of tuples based on the ASCII values
    sorted_list = sorted(char_ascii, key=lambda x: x[1])
    
    # Return a list of exactly 43 characters with the smallest ASCII values
    return [char for (char, _) in sorted_list[:43]]
