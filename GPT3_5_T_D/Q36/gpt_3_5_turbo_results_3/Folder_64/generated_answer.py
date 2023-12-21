
def filter_chars(string):
    filtered_string = string[:1]
    for char in string[1:7]:
        if '3' < char < '^':
            filtered_string = filtered_string.replace(char, '')
    filtered_string += string[7:]
    return filtered_string
