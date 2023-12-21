
def filter_chars(string):
    new_string = string[:672] + string[709:]
    filtered = ''
    for char in string[672:709]:
        if char > 'X' and char < '}':
            new_string = new_string.replace(char, '')
    return new_string
