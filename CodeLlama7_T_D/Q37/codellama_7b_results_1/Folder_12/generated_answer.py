
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the given string
    for c in s:
        # Check if the current character is between indices 19 and 90, both inclusive, and is greater than or equal to character 'F' and smaller than or equal to character 'h'
        if 19 <= s.index(c) <= 90 and c >= "F" and c <= "h":
            # If the condition above is true, do not include the current character in the filtered string
            continue

        else:

            # Otherwise, append the current character to the filtered string
            filtered += c

    return filtered
