
def filter_chars(string):
    result = ''
    for char in string:
        if char > 'S' and char < '[':
            continue
        else:
            result += char
    return result
