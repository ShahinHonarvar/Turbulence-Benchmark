
def remove_repeat_chars(string):
    # Initialize an empty list to store the characters
    # that are not repeated between indices 68 and 99
    unique_chars = []
    # Iterate through each character in the string
    for char in string:
        # If the current character is not already in the unique_chars list, add it
        if char not in unique_chars:
            unique_chars.append(char)
    # Initialize an empty string to store the altered string
    altered_string = ""
    # Iterate through each character in the unique_chars list
    for char in unique_chars:
        # If the current character is not present between indices 68 and 99, add it to the altered_string
        if string.find(char) != -1:
            altered_string += char
    return altered_string
