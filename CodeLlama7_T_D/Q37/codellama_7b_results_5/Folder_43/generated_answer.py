
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over the characters in the given string
    for char in string:
        # Check if the current character is between indices 15 and 55, both inclusive
        if 15 <= string.index(char) <= 55:
            # Check if the current character is greater than or equal to 'W' and smaller than or equal to '{', both inclusive
            if char >= 'W' and char <= '{':
                continue

        # If the current character does not meet the criteria, add it to the filtered characters list
        else:
            filtered_chars.append(char)

    # Join the filtered characters into a string
    filtered_string = ''.join(filtered_chars)

    # Return the altered string
    return filtered_string
