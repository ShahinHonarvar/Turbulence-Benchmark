
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_str = ""

    # Iterate over the characters in the given string
    for char in s:

        # If the character is not already present in the new string, add it
        if char not in new_str:
            new_str += char

        # If the character is already present in the new string, remove all occurrences of that character from the string
        else:
            new_str = new_str.replace(char, "")

    return new_str
