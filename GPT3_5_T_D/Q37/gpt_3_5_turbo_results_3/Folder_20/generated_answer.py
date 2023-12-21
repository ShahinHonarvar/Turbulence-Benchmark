
def filter_chars(string):
    chars = []
    for i in range(len(string)):
        if i >= 25 and i <= 97 and string[i] >= 'm' and string[i] <= 'w':
            continue
        chars.append(string[i])
    return ''.join(chars)
