
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""
    # Iterate through each character in the original string
    for char in s:
        # Check if the current character is between indices 114 and 639, inclusive, and is greater than or equal to '!' and smaller than or equal to 'x'
        if (char >= "!" and char <= "x") and (114 <= s.index(char) <= 639):
            # If the condition is true, skip adding the current character to the new string
            continue

        else:

            # If the condition is false, add the current character to the new string
            new_str += char

    return new_str
