
def filter_chars(string):
    chars_to_remove = string[38:81]
    for char in chars_to_remove:
        if '.' < char < '^':
            string = string.replace(char, '')
    return string
