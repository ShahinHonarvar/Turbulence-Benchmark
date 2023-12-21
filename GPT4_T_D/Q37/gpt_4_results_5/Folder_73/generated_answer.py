
def filter_chars(s):
    output = s
    for ch in s[22:86]:
        if '7' <= ch <= 'e':
            output = output.replace(ch, '')
    return output
