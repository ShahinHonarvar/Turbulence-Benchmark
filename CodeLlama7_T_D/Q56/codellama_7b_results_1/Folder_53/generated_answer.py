
def all_substring_of_size_n(string):
    """Returns a list of all distinct substrings of length n in the given string. If no such substrings exist, returns an empty list."""
    # Initialize result list and count of characters in substring
    result = []
    count = 0

    # Iterate over each character in the given string
    for char in string:
        # Increment count of characters in substring if current character is not a space
        if char != ' ':
            count += 1

        # If current character is a space or we have reached the end of the string, check if substring has length n and add it to result list
        elif char == ' ' or count == n:
            # Add substring to result list if it exists
            if count == n:
                result.append(''.join(string[i:i+n]))

            # Reset count of characters in substring
            count = 0

    return result
