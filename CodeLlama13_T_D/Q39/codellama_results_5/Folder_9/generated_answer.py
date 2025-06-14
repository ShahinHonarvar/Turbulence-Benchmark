
def return_n_greatest_chars(string):
    # Create a dictionary to store the character and its ASCII value
    char_ascii = {}
    for char in string:
        if char not in char_ascii:
            char_ascii[char] = ord(char)
    
    # Sort the dictionary by the ASCII values in descending order
    sorted_chars = sorted(char_ascii.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top 20 characters with the greatest ASCII values
    return [char for char, ascii_value in sorted_chars[:20]]
