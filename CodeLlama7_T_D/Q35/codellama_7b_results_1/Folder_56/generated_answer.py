
def remove_repeat_chars(s):
    # Create a dictionary to keep track of repeated characters
    char_dict = {}

    # Iterate over the string and check for repeated characters
    for i in range(len(s)):
        if s[i] in char_dict:
            # If the character is repeated, remove all occurrences from the string
            while s[i] in s[i+1:]:
                s = s[:i] + s[i+1:]

    # Return the altered string
    return s
