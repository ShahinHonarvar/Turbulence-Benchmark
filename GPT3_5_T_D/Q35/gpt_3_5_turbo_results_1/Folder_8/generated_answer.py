
def remove_repeat_chars(string):
    indices = range(46, 48)
    unique_chars = set()
    for index in indices:
        char = string[index]
        if char not in unique_chars and string.count(char) > 1:
            unique_chars.add(char)
            string = string.replace(char, '')
    return string
