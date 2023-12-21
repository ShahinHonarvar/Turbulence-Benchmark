
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the given string
    for char in s:

        # Check if the current character is between indices 227 and 235, both inclusive
        if (char >= 'D' and char <= 'u') or (char >= 'd' and char <= 'u'):

            # If the current character is within the specified range, add it to the filtered_chars list
            filtered_chars.append(char)

    # Join the filtered characters together into a single string
    filtered_string = "".join(filtered_chars)

    # Return the altered string
    return filtered_string
