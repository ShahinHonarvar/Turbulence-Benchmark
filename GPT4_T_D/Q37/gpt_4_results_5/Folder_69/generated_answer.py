
def filter_chars(s):
    altered_s = s
    for char in s[114:640]:
        if '!' <= char <= 'x':
            altered_s = altered_s.replace(char, '')
    return altered_s
