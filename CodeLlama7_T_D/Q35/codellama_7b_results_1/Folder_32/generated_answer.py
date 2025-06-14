
def remove_repeat_chars(s):
    # create a set of unique characters in the string
    unique_chars = set(s)
    # initialize an empty string to store the altered string
    altered_string = ""

    # iterate over each character in the string
    for char in s:
        # if the character is not already in the unique_chars set, add it and append it to the altered_string
        if char not in unique_chars:
            unique_chars.add(char)
            altered_string += char

    # return the altered string
    return altered_string
