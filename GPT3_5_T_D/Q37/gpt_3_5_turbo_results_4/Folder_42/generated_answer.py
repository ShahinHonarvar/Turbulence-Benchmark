
def filter_chars(string):
    for char in string[73:75]:
        if char >= 'U' and char <= 'l':
            string = string.replace(char, "")
    return string
