
def remove_repeat_chars(string):
    # create a list of all unique characters in the string
    unique_chars = set(string)
    # for each character that occurs more than once between indices 81 and 86, both exclusive, remove all occurrences of that character from the string
    for char in unique_chars:
        if string.count(char) > 1 and (char not in string[0:81] or char not in string[87:]):
            string = string.replace(char, "")
    return string
