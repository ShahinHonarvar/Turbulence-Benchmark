
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ''
    
    # Loop through each character in the original string
    for char in s:
        # If the current character is between indices 18 and 95 (both exclusive)
        if ord(char) > 74 and ord(char) < 96:
            # If the current character is greater than 'K' and smaller than 'a', remove it from the string
            new_str += char
            
    return new_str
