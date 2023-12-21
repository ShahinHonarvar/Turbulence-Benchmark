
def remove_repeat_chars(s):
    # Create a new string that will contain the altered characters
    new_string = ""

    # Iterate over each character in the given string
    for i in range(len(s)):
        # If the current character is not repeated between indices 200 and 202, exclusive, add it to the new string
        if s[i] not in s[200:202]:
            new_string += s[i]

    # Return the altered string with the repeated characters removed
    return new_string
