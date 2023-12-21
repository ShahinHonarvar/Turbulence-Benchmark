
def return_n_greatest_chars(string):
    # Create a list of tuples containing each character and its ASCII value
    char_ascii = [(char, ord(char)) for char in string]
    
    # Sort the list by the second element (ASCII value) in descending order
    sorted_chars = sorted(char_ascii, key=lambda x: x[1], reverse=True)
    
    # Return the first 13 characters of the sorted list
    return [char for char, _ in sorted_chars[:13]]
