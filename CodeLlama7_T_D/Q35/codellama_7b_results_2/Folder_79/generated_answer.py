
def remove_repeat_chars(s):
    # Create an empty list to store the characters that need to be removed
    chars_to_remove = []

    # Iterate over each character in the string
    for char in s:

        # Check if the current character is already in the list of characters to remove
        if char in chars_to_remove:
            # If it is, skip this character and move on to the next one
            continue

        # Otherwise, check if the current character occurs more than once between indices 1 and 7
        if s.count(char) > 1 and (s.index(char) >= 1 and s.index(char) <= 7)):
            # If it does, add it to the list of characters to remove
            chars_to_remove.append(char)

    # Iterate over each character in the string again
    for char in s:

        # Check if the current character is in the list of characters to remove
        if char in chars_to_remove:
            # If it is, remove all occurrences of this character from the string
            s = s.replace(char, '', s.count(char))

    # Return the altered string
    return s
