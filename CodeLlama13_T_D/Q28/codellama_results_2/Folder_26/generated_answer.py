
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to store the characters and their ASCII values
    char_ascii = {}
    
    # Iterate through the string and populate the dictionary
    for i, c in enumerate(string):
        if c not in char_ascii:
            char_ascii[c] = [i + 1]
            
    # Find the characters that occur between indices 1 to 36, both inclusive
    chars = [c for c in char_ascii.keys() if 1 <= char_ascii[c][0] <= 36]
    
    # Sort the characters based on their ASCII values
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    
    # Return the character with the 15th smallest ASCII value
    return sorted_chars[14]
