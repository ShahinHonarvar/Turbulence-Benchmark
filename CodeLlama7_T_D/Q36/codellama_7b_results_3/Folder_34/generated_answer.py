
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over the characters in the given string
    for char in s:
        # Check if the current character is between indices 10 and 79 (both exclusive)
        if 10 < ord(char) < 79:
            # If the current character is greater than '?' and smaller than 'm', remove all occurrences of that character within the string
            filtered_chars.append(char) if char not in filtered_chars else filtered_chars
    return "".join(filtered_chars)
