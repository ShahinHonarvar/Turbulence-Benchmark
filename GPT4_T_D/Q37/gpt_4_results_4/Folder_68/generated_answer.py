
def filter_chars(s):
    filtered_chars = [char for char in s[7:10] if char >= '6' and char <= 'w']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
