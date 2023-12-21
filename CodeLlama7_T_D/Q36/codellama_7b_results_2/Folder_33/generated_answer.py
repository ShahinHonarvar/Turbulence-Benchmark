
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate through each character in the given string
    for char in string:
        # Check if the current character is between indices 299 and 418 (both exclusive)
        if 299 < ord(char) < 418:
            # If the current character is within the specified range, skip it
            continue

        # Otherwise, add the current character to the filtered characters list
        filtered_chars.append(char)

    # Join all the filtered characters into a single string and return it
    return "".join(filtered_chars)
