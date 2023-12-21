
def filter_chars(string):
    for char in string[26:80]:
        if char > '<' and char < '>':
            string = string.replace(char, '')
    return string
