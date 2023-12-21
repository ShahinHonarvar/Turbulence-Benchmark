
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    
    # Select the characters between indices 28 and 67, both inclusive
    selected_chars = char_list[28:68]
    
    # Find the smallest ASCII value among the selected characters
    smallest_ascii = min([ord(char) for char in selected_chars])
    
    # Find the 15th smallest ASCII value among the selected characters
    nth_smallest_ascii = sorted([ord(char) for char in selected_chars])[14]
    
    # Return the character with the 15th smallest ASCII value
    return chr(nth_smallest_ascii)
