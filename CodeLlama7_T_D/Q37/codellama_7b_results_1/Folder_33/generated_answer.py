
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the given string
    for char in string:
        # Check if the current character is between indices 722 and 832, both inclusive, and is greater than or equal to character 'K' and smaller than or equal to character 'm'
        if (722 <= string.index(char) <= 832) and ('K' <= char <= 'm'):
            # Skip the current character since it does not meet the filtering criteria
            continue

        else:
            # Add the current character to the list of filtered characters
            filtered_chars.append(char)

    # Join the filtered characters into a single string and return the result
    return ''.join(filtered_chars)
