
def filter_chars(string):
    # Create a list of characters in the string
    char_list = list(string)
    # Iterate over the characters between indices 35 and 89, inclusive
    for i in range(35, 90):
        # If the current character is greater than or equal to 'E' and smaller than or equal to 't', remove it from the string
        if char_list[i] >= 'E' and char_list[i] <= 't':
            del char_list[i]
    # Return the altered string
    return "".join(char_list)
