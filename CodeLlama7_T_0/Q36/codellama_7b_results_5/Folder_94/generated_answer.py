
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between 15 and 85 (exclusive)
        if 15 < ord(char_list[i]) < 85:
            # If it is, check if it is greater than 'I' and smaller than 'M'
            if char_list[i] > 'I' and char_list[i] < 'M':
                # If it is, remove all occurrences of that character in the string
                char_list = [char for char in char_list if char != char_list[i]]
    # Return the altered string
    return "".join(char_list)
