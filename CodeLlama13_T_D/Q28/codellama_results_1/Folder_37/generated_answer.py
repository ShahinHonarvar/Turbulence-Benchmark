
def return_nth_smallest_ascii(string):
    # Create a list of characters in the string
    chars = []
    for i in range(28, 67 + 1):
        if string[i] not in chars:
            chars.append(string[i])
    
    # Sort the list of characters by ASCII value
    sorted_chars = sorted(chars)
    
    # Return the nth character (here, 15th smallest ASCII value)
    return sorted_chars[14]
