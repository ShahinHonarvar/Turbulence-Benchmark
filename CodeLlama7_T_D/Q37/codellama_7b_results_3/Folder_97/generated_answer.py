
def filter_chars(s):
    # Create a new string with the filtered characters
    new_string = ""

    # Iterate through each character in the given string
    for char in s:
        # If the current character is between indices 227 and 235, both inclusive, and is greater than or equal to 'D' and smaller than or equal to 'u', then add it to the new string
        if (ord(char) >= 227 and ord(char) <= 235) and ('D' <= char <= 'u'):
            new_string += char

    # Return the altered string with all occurrences of filtered characters removed while preserving their original order.
    return new_string
