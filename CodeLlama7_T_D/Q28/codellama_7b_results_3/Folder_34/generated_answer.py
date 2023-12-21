
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the character with the 19th smallest ASCII value
    nth_smallest_ascii = sorted(char_list, key=ord)[18]
    return nth_smallest_ascii
