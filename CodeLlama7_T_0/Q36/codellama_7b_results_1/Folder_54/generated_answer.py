
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters between indices 18 and 38 (both exclusive)
    for i in range(18, 38):
        # If the current character is greater than ')' and smaller than 'P', remove all occurrences of that character within the string
        if char_list[i] > ')' and char_list[i] < 'P':
            char_list.remove(char_list[i])
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
