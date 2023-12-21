 def remove_repeat_chars(s):
    # create a list of characters in the given string
    char_list = list(s)
    # initialize an empty string to store the altered string
    altered_string = ""
    # iterate over each character in the list
    for char in char_list:
        # if the current character is not already present in the altered string, append it
        if char not in altered_string:
            altered_string += char
    return altered_string
