
def filter_chars(string):
    chars_to_filter = [char for char in string[4:5] if char >= '7' and char <= 'o']
    for char in chars_to_filter:
        string = string.replace(char, '')
    return string
