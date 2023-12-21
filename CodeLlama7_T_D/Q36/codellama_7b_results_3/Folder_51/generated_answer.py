
def filter_chars(s):
    # Create a new string with the filtered characters
    new_string = ""
    # Iterate over each character in the original string
    for char in s:
        # If the current character is between 58 and 81 (exclusive) and it is not ">" or "<", then add it to the new string
        if char.isdigit() and int(char) >= 58 and int(char) <= 81 and char != ">":
            new_string += char
    # Return the altered string
    return new_string
