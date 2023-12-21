
def filter_chars(strng):
    new_chars = []
    for char in strng[41:80]:
        if char >= 'f' and char <= '|':
            new_chars.append(char)
    result = ''
    for char in strng:
        if char not in new_chars:
            result += char
    return result
