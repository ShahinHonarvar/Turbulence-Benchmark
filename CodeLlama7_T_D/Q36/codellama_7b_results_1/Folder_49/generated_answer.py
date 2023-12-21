
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 46 and 91 (exclusive)
        if 46 < ord(char_list[i]) < 91:
            # If the current character is greater than 'D' and smaller than 'H', remove all occurrences of that character in the string
            while char_list[i] in char_list:
                char_list.remove(char_list[i])
    return "".join(char_list)
