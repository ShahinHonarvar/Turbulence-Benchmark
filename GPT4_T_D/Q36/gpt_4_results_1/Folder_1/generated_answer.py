
def filter_chars(s):
    to_remove = []
    for char in s[70:87]:
        if '#' < char < 'L':
            to_remove.append(char)
    
    for char in to_remove:
        s = s.replace(char, '')

    return s
