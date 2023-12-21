 def filter_chars(s):
    # Initialize a new empty string
    result = ""

    # Iterate through each character in the input string
    for c in s:
        # If the current character is between indices 373 and 901, both inclusive, and is greater than or equal to character 'T' and smaller than or equal to character 'h', then remove all occurrences of that character from the input string
        if (373 <= s.find(c) <= 901) and (ord('T') <= ord(c) <= ord('h')):
            # Skip the current character
            continue

        # Otherwise, append the current character to the result string
        else:
            result += c

    # Return the altered input string
    return result
