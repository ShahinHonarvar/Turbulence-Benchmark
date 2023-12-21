
def remove_repeat_chars(s):
    # Create a dictionary to keep track of the characters in the string
    char_dict = {}
    # Iterate over each character in the string
    for char in s:
        # If the current character has already been seen before,
        if char in char_dict:
            # Remove all occurrences of the current character from the string
            s = s.replace(char, "")
        # Otherwise, add the current character to the dictionary
        else:
            char_dict[char] = True
    return s
