
def filter_chars(string):
    # Create a list of characters from the input string
    chars = list(string)
    
    # Iterate through the list of characters and remove those between indices 318 and 337
    for i in range(318, 337):
        if i < len(chars) and chars[i] > 'B' and chars[i] < 'z':
            chars.remove(chars[i])
    
    # Return the altered string
    return ''.join(chars)
