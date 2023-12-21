
def filter_chars(string):
    chars = list(string)
    for i in range(3, 9):
        if chars[i] > '*' and chars[i] < 'E':
            chars = [c for c in chars if c != chars[i]]
    return "".join(chars)
