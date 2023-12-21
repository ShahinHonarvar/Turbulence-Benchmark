
def filter_chars(string):
    # Create a list of characters between indices 170 and 195 (exclusive)
    char_list = string[170:195]
    # Remove all occurrences of the character '!' from the list
    char_list = [char for char in char_list if char != '!']
    # Remove all occurrences of the character '}' from the list
    char_list = [char for char in char_list if char != '}']
    # Create a new string by joining the filtered characters together
    filtered_string = "".join(char_list)
    return filtered_string
