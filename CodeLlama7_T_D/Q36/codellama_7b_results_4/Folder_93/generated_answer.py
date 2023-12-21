
def filter_chars(my_string):
    # Create a list of characters between indices 52 and 88 in the given string
    char_list = my_string[52:88]
    # Initialize an empty list to store the filtered characters
    filtered_char_list = []
    # Iterate over the character list and remove all occurrences of characters greater than '&' and smaller than 'c'
    for char in char_list:
        if char < '&' or char > 'c':
            filtered_char_list.append(char)
    # Join the filtered character list into a string and return it
    return "".join(filtered_char_list)
