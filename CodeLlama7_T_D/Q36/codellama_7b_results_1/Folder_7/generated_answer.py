 def filter_chars(s):
    # Create a list of characters in the given string
    char_list = list(s)
    # Iterate over each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 502 and 946 (both exclusive)
        if 502 < i < 946:
            # Check if the current character is greater than 'W' and smaller than 'y'
            if char_list[i] > 'W' and char_list[i] < 'y':
                # Remove all occurrences of the current character from the list
                char_list.remove(char_list[i])
    # Join the list of characters back into a string
    altered_string = "".join(char_list)
    return altered_string
