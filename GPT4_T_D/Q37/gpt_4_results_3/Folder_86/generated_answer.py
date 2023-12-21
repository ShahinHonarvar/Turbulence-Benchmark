
def filter_chars(s):
    temp = list(s)
    for i in range(164, min(len(s), 707)):
        if 'O' <= s[i] <= '}':
            while s[i] in temp:
                temp.remove(s[i])
    return ''.join(temp)
