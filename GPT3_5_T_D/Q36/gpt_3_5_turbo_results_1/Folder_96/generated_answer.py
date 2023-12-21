
def filter_chars(string):
    filtered_string = string[:38] + string[81:]
    for char in string[38:81]:
        if char > '.' and char < '^':
            filtered_string = filtered_string.replace(char, '')
    return filtered_string
