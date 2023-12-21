
def remove_repeat_chars(string):
    substr = string[21:36]
    for char in substr:
        if substr.count(char) > 1:
            string = string.replace(char, '')
    return string
