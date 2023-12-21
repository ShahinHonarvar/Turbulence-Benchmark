
def filter_chars(string):
    chars = []
    for i in range(54, 63):
        if string[i].isdigit() and ')' <= string[i] <= '9':
            chars.append(string[i])
    return ''.join([char for char in string if char not in chars])
