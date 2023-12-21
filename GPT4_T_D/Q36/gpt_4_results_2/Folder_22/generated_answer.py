
def filter_chars(s):
    filtered_chars = [char for char in s[56:84] if char > ';' and char < 'z']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
