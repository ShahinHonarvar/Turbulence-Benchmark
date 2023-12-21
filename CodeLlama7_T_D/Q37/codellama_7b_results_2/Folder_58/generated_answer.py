
def filter_chars(s):
    # Create a new empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the original string
    for c in s:
        # If the current character is between indices 503 and 753, both inclusive, and is greater than or equal to character '9' and smaller than or equal to character 'w', then remove it from the filtered string
        if (c >= "9" and c <= "w") and (503 <= s.index(c) <= 753)):
            continue

        # Otherwise, add the current character to the filtered string
        else:
            filtered += c

    # Return the filtered string
    return filtered
