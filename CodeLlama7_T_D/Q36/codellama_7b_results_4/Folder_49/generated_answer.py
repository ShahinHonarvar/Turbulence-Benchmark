
def filter_chars(s):
    # Create a new string with the filtered characters
    new_string = ""

    # Iterate through each character in the given string
    for char in s:
        # If the current character is between 46 and 91 (exclusive)
        if ord(char) >= 46 and ord(char) < 91:
            # Check if the character is greater than 'D' and smaller than 'H'
            if char > 'D' and char < 'H':
                # Remove all occurrences of this character from the new string
                new_string = new_string.replace(char, "")
        else:
            # If the current character is not between 46 and 91 (exclusive), append it to the new string
            new_string += char

    return new_string
