
def filter_chars(s):
    altered_s = s
    for ch in s[164:658]:
        if '(' < ch < ']':
            altered_s = altered_s.replace(ch, '')
    return altered_s
