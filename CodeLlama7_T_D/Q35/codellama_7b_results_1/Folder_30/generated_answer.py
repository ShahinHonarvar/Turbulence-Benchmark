
def remove_repeat_chars(s):
    # Create a dictionary to keep track of repeated characters
    repeated_chars = {}

    # Loop through the string and check for repeated characters
    for i in range(len(s)):
        if s[i] in repeated_chars:
            # If the character is repeated, remove all occurrences from the string
            while s[i] in repeated_chars:
                s = s[:i] + s[i+1:]
            # Update the dictionary to reflect the change
            repeated_chars[s[i]] = i
        else:
            # If the character is not repeated, add it to the dictionary
            repeated_chars[s[i]] = i

    # Return the altered string
    return s
