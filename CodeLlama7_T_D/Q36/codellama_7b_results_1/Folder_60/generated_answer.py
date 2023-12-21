 def filter_chars(s):
    # Create a new string with the same length as the original string
    new_string = ""
    for i in range(len(s)):
        # If the current character is between the indices 23 and 83 (both exclusive)
        if 23 < i < 83:
            # If the current character is greater than character 'f' and smaller than character 'o'
            if s[i] > 'f' and s[i] < 'o':
                # Skip this character in the new string
                continue

        # Add the current character to the new string
        new_string += s[i]
    return new_string
