
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the given string
    for char in string:
        # Check if the current character is between indices 32 and 46, inclusive
        if 32 <= ord(char) <= 46:
            # Check if the current character is greater than or equal to '0' and smaller than or equal to 'k'
            if char >= "0" and char <= "k":
                # If both conditions are true, append the filtered character to the string
                filtered += char

    return filtered
