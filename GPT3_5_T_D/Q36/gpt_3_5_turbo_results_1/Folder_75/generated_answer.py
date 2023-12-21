
def filter_chars(string):
    filtered_string = string[:46]
    filtered_string += string[74:]
    for char in string[46:74]:
        if ord('&') < ord(char) < ord('M'):
            filtered_string = filtered_string.replace(char, '')
    return filtered_string
