
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters between indices 10 and 15 (both exclusive)
    for i in range(10, 15):
        # If the current character is greater than 't' and smaller than 'v', remove all occurrences of that character within the string
        if char_list[i] > 't' and char_list[i] < 'v':
            char_list.remove(char_list[i])
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
