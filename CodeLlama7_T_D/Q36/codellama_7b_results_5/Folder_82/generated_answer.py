
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered = ""
    
    # Loop through each character in the given string
    for char in string:
        # If the current character is between 69 and 97 (both exclusive)
        if 69 < ord(char) < 97:
            # And it is greater than 'V' and smaller than 'j'
            if ord(char) > ord('V') and ord(char) < ord('j'):
                # Do not add this character to the filtered string
                continue
                
        # Add the current character to the filtered string
        filtered += char
    
    # Return the filtered string
    return filtered
