
def filter_chars(s):
    # Create an empty string to hold the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for c in s:
        # Check if the current character should be removed from the output string
        if (c >= "L" and c <= "a") or (c == "L" or c == "a"):
            # Skip adding this character to the filtered string
            continue

        # Add the current character to the filtered string
        filtered += c

    # Return the filtered string
    return filtered
