 def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate through each character in the given string
    for char in s:
        # If the current character is between indices 1 and 7, both inclusive, and is greater than or equal to character 'L' and smaller than or equal to character 'a', then remove all occurrences of that character from the string
        if (char >='L') & (char <= 'a')):
            filtered = filtered + char

    # Return the altered string
    return filtered
