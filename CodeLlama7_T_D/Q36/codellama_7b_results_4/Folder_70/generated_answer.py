
def filter_chars(string):
    # Create a list of characters between indices 170 and 195 (exclusive)
    char_list = string[170:195]
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    for char in char_list:
        if not (char > '!' and char < '}'):
            filtered_string += char

    return filtered_string
