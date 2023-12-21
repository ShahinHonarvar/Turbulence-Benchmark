
def filter_chars(string):
    chars = []
    for i in range(50, 92):
        if string[i].isalpha() and 'A' <= string[i] <= 'Q':
            chars.append(string[i])
    return ''.join([char if char not in chars else '' for char in string])
