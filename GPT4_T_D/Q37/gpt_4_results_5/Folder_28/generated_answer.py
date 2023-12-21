
def filter_chars(str):
    for ch in str[20:80]:
        if ch >= '!' and ch <= 'T':
            str = str.replace(ch, '')
    return str
