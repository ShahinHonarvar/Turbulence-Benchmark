
def filter_chars(s):
    char_list = [ch for ch in s[12:46] if '!' < ch < 'A']
    for ch in char_list:
        s = s.replace(ch, '')
    return s
