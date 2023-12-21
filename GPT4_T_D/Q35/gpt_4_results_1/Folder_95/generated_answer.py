
def remove_repeat_chars(string):
    substring = string[33:99]
    for char in substring:
        if substring.count(char) > 1:
            string = string.replace(char, '')
    return string
