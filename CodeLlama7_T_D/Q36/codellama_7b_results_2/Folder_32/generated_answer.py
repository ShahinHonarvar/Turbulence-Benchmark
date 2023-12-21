 def filter_chars(s):
    # Initialize a new empty string
    filtered = ""

    # Iterate over each character in the input string
    for char in s:
        # If the current character is between 40 and 63 (exclusive)
        if ord(char) >= 40 and ord(char) < 63:
            # And it's not between 7 and 10
            if ord(char) <= 7 or ord(char) >= 10:
                # Then append the current character to the filtered string
                filtered += char

    # Return the filtered string
    return filtered
