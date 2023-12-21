
def filter_chars(string):
    start = 331
    end = 713
    if start < end and start >= 0 and end <= len(string):
        chars_to_remove = []
        for i in range(start, end):
            if 'M' < string[i] < '_':
                chars_to_remove.append(string[i])
        for char in chars_to_remove:
            string = string.replace(char, '')
    return string
