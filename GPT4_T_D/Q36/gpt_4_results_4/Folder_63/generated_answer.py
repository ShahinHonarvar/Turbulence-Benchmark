
def filter_chars(str):
    for ch in str[27:80]:
        if ch > '<' and ch < '>':
            str = str.replace(ch, '')
    return str
