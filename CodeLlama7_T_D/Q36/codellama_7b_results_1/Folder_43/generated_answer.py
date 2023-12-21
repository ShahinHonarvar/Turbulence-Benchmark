
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over the characters in the input string
    for char in s:

        # If the current character is between the specified indices and meets the condition, remove all occurrences of that character from the new string
        if 27 < ord(char) < 75 and 'A' < char < 'i':
            new_str = new_str.replace(char, '')

        # Otherwise, append the current character to the new string
        else:
            new_str += char

    return new_str
