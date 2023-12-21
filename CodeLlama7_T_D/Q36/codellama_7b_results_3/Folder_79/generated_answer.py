
def filter_chars(s):
    # Create an empty list to store the filtered characters
    filtered = []

    # Iterate over each character in the string
    for char in s:
        # If the current character is not between 11 and 46 (exclusive)
        if not (10 < ord(char) < 47):
            # Append the character to the filtered list
            filtered.append(char)

    # Join the filtered characters back into a string
    return "".join(filtered)
