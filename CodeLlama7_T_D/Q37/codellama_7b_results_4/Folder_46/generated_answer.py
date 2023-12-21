
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over each character in the list
    for i, c in enumerate(char_list):
        # Check if the current character is between indices 11 and 72, both inclusive, and is greater than or equal to character 'i' and smaller than or equal to character 'v'
        if 11 <= i <= 72 and c >= 'i' and c <= 'v':
            # Remove all occurrences of the current character from the list
            char_list = [x for x in char_list if x != c]
    # Join the filtered characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
