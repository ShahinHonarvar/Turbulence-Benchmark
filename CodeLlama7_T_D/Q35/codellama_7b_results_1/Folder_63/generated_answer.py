
def remove_repeat_chars(s):
    # create a new string with the characters removed
    new_str = ""
    # iterate over the characters in the given string
    for char in s:
        # if the character is not present in the substring between indices 81 and 86, exclusive, then append it to the new string
        if not new_str.endswith(char):
            new_str += char
    return new_str
