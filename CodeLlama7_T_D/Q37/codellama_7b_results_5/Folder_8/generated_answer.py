
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate over each character in the string
    for char in string:
        # Check if the character is between indices 41 and 86, both inclusive, and is greater than or equal to character 'S' and smaller than or equal to character 's'
        if (41 <= ord(char) <= 86) and ('S' <= char <= 's'):
            # If the condition is true, add the character to the filtered_chars list
            filtered_chars.append(char)
    # Join the filtered characters into a string and return it
    return "".join(filtered_chars)
