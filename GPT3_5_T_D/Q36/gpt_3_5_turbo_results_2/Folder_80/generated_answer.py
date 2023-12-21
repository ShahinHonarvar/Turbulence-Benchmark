
def filter_chars(string):
    chars_to_remove = ''
    for i in range(54, 92):
        if 'J' < string[i] < 'X':
            chars_to_remove += string[i]
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
