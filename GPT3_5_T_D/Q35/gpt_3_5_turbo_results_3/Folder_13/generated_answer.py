
def remove_repeat_chars(string):
    unique_chars = []
    for char in string:
        if string.count(char) > 1 and 46 < string.index(char) < 91:
            continue
        unique_chars.append(char)
    return ''.join(unique_chars)
