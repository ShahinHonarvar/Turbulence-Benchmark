
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over the characters in the input string
    for char in s:
        # Check if the current character is between 343 and 665 (both exclusive)
        if 343 < ord(char) < 665:
            # If it is, add the character to the list of filtered characters
            filtered_chars.append(char)

    # Join the filtered characters back into a string and return it
    return "".join(filtered_chars)
