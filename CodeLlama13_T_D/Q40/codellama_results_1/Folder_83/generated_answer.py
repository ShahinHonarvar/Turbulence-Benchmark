
def return_n_smallest_chars(string):
    # Create a dictionary to store character: ASCII value pairs
    char_ascii = {}
    for char in string:
        ascii_val = ord(char)
        char_ascii[char] = ascii_val
    
    # Sort the dictionary by ASCII values in descending order
    sorted_chars = sorted(char_ascii.items(), key=lambda x: x[1], reverse=True)
    
    # Return a list of 38 characters with smallest ASCII values
    return [char for char, _ in sorted_chars[:38]]
