
def filter_chars(string):
    filtered_string = string[:82]
    for char in string[82:89]:
        if char > '*' and char < '[':
            filtered_string = filtered_string.replace(char, '')
    filtered_string += string[89:]
    return filtered_string
