
def remove_repeat_chars(s):
    # create a set of unique characters in the string
    unique_chars = set(s)
    # initialize an empty string to store the altered string
    altered_string = ""

    for char in s:

        # if the character is not in the set of unique characters, append it to the altered string
        if char not in unique_chars:
            altered_string += char

        # otherwise, do nothing and move on to the next character
        else:
            continue

    return altered_string
