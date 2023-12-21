
def remove_repeat_chars(s):
    # Initialize a new string to store the altered characters
    new_string = ""

    # Iterate over each character in the given string
    for char in s:
        # If the current character is not present more than once between indices 80 and 200, exclusive, then append it to the new string
        if s.count(char) == 1 or (s.index(char) > 80 and s.index(char) < 200)):
            new_string += char

    # Return the altered string
    return new_string
