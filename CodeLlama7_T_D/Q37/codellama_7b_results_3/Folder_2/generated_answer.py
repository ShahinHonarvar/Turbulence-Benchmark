
def filter_chars(s):
    # Create a new string with all characters removed
    result = ""

    # Iterate over each character in the original string
    for c in s:

        # If the current character is not in the range of interest (i.e., between indices 477 and 984, both inclusive), then add it to the new string
        if c < "," or c > "V":
            result += c

    return result
