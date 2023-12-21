 def filter_chars(s):
    # Create a new string with the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for c in s:

        # Check if the current character is between indices 22 and 85, both inclusive, and is greater than or equal to character '7' and smaller than or equal to character 'e'
        if (22 <= s.index(c) <= 85) and ('7' <= c <= 'e'):

            # If the current character meets the condition, skip it in the filtered string
            continue

        # Otherwise, add the current character to the filtered string
        filtered += c

    # Return the filtered string
    return filtered
