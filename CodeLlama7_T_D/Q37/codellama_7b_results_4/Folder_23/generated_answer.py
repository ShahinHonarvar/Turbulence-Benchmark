 def filter_chars(s):
    # Create a new string with the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for char in s:

        # If the current character is between indices 51 and 77, both inclusive, and is greater than or equal to 'V' and smaller than or equal to 'Y', then remove it from the filtered string
        if 50 <= len(filtered) <= 78 and 'V' <= char <= 'Y':
            continue

        # Otherwise, append the character to the filtered string
        filtered += char

    # Return the filtered string
    return filtered
