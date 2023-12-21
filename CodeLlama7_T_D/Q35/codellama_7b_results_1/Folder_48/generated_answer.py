
def remove_repeat_chars(s):
    # create a set of unique characters in the string
    unique_chars = set()
    # iterate over each character in the string
    for char in s:
        # if the character is not already in the set, add it
        if char not in unique_chars:
            unique_chars.add(char)
    # create a new string with the unique characters only
    new_string = ""
    for char in unique_chars:
        new_string += char
    return new_string
