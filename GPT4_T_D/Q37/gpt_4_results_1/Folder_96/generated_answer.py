
def filter_chars(s):
    chars_to_remove = [char for char in s[86:93] if '!' <= char <= 's']
    res = ''
    for char in s:
        if char not in chars_to_remove:
            res += char
    return res
