
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the string
    for char in s:

        # If the current character is between indices 18 and 64 (both exclusive) and is greater than '3' and smaller than 'B', then remove all occurrences of that character from the string
        if 18 < ord(char) < 64 and ord('3') < ord(char) < ord('B'):
            filtered_chars.append(char)

    # Return the altered string with the filtered characters removed
    return ''.join(filtered_chars)
