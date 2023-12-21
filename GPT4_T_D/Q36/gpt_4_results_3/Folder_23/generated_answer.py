
def filter_chars(in_str):
    for ch in in_str[22:25]:
        if '5' < ch < '}':
            in_str = in_str.replace(ch, '')
    return in_str
