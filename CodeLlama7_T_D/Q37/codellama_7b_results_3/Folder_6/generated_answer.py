
def filter_chars(string, c, n):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the string
    for char in string:
        # If the current character is between indices 13 and 28 (inclusive) and is greater than or equal to 'c' and smaller than or equal to 'n', add it to the filtered_chars list
        if (char >= c and char <= n) and (char.lower() in range(ord('a'), ord('z') + 1)):
            filtered_chars.append(char)
    # Join the filtered characters into a string and return it
    return ''.join(filtered_chars)
