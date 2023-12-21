
def filter_chars(string):
    new_str = ''
    for char in string:
        if char != '(' and char != ')' and char != '[' and char != ']':
            new_str += char
    return new_str
