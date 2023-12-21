
def filter_chars(string):
    # Create a list of characters between indices 323 and 526 (both exclusive) in the given string
    char_list = string[323:526]
    # Initialize an empty list to store the filtered characters
    filtered_char_list = []
    # Iterate over each character in the list of characters between indices 323 and 526 (both exclusive) in the given string
    for char in char_list:
        # If the current character is greater than character ')' and smaller than character 'O', remove all occurrences of that character within the string while keeping the order of all characters in the string intact.
        if char > ')' and char < 'O':
            filtered_char_list.append(char)
    # Return the altered string with the filtered characters
    return ''.join(filtered_char_list)
