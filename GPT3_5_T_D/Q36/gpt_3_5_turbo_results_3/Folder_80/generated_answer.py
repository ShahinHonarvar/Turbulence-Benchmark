
def filter_chars(string):
    filtered_string = string[:54] + string[92:]
    for char in string[54:92]:
        if 'J' < char < 'X':
            filtered_string = filtered_string.replace(char, '')
    return filtered_string
