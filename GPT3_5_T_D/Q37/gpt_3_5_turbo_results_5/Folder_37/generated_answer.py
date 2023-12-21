
def filter_chars(string):
    for char in string[17:64]:
        if char >= 'O' and char <= '^':
            string = string.replace(char, "")
    return string
