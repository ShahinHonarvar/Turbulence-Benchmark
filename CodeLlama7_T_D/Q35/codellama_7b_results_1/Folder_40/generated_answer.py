 def remove_repeat_chars(s):
    # Initialize a new string to store the modified characters
    new_str = ""
    # Iterate through each character in the given string
    for char in s:
        # Check if the current character has already been added to the new string
        if char not in new_str:
            # If not, add it to the new string and continue with the next character
            new_str += char
        # If the current character has already been added to the new string, check if there are any subsequent occurrences of that character
        else:
            # If there are, find the index of the last occurrence and remove all characters after that index from the new string
            idx = new_str.rfind(char)
            new_str = new_str[:idx]
    return new_str
