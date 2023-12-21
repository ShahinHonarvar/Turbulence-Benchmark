
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for c in s:

        # Check if the current character is between indices 29 and 79, both inclusive, and is greater than or equal to character 'K' and smaller than or equal to character 'z'
        if (c >= 'K' and c <= 'z') and (c.index(c) >= 29 and c.index(c) <= 79):

            # If the current character meets the condition, add it to the filtered string
            filtered += c

    return filtered
