
def return_nth_smallest_ascii(string):
    # Extract the substring between indices 60 and 83
    substring = string[60:84]
    
    # Sort the characters in the substring by ASCII value
    sorted_chars = sorted(substring)
    
    # Return the character at the 14th index
    return sorted_chars[13]
